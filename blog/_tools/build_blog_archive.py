#!/usr/bin/env python3
"""Build the Digital History Hacks archive from the Blogger feed.

Usage:
    python3 blog/_tools/build_blog_archive.py fetch   # download feed JSON to blog/_tools/feed/
    python3 blog/_tools/build_blog_archive.py images  # copy post images to blog/images/
    python3 blog/_tools/build_blog_archive.py build   # write blog/posts/*.md and blog/README.md

Each post becomes blog/posts/YYYYMMDD-slug.md. Every hyperlink in a post is
replaced by a numbered Markdown footnote, and the footnote shows the original
URL as plain text. Images point to local copies in blog/images/ once the
`images` step has downloaded them (otherwise to the original Blogger copy).
Code passages become fenced code blocks, and each post ends with links to
the previous (older) and next (newer) posts.

Folders whose names start with "_" are ignored by GitHub Pages, so this
script and the cached feed are not published on the website.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

BLOG = "https://digitalhistoryhacks.blogspot.com"
HERE = Path(__file__).resolve().parent
FEED_DIR = HERE / "feed"
BLOG_DIR = HERE.parent
POSTS_DIR = BLOG_DIR / "posts"
IMAGES_DIR = BLOG_DIR / "images"
IMAGE_MANIFEST = HERE / "images.json"     # original image URL -> local file
PAGE_SIZE = 150


# ---------------------------------------------------------------- fetching

def fetch():
    FEED_DIR.mkdir(exist_ok=True)
    start, page = 1, 1
    while True:
        url = (f"{BLOG}/feeds/posts/default?alt=json"
               f"&max-results={PAGE_SIZE}&start-index={start}")
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        entries = data["feed"].get("entry", [])
        if not entries:
            break
        (FEED_DIR / f"page-{page:02d}.json").write_text(
            json.dumps(data, ensure_ascii=False))
        print(f"page {page}: {len(entries)} posts")
        start += len(entries)
        page += 1


def image_sources(html):
    """Yield (img src, best URL to download) for each image in a post.
    Blogger wraps each picture in a link to a larger copy; use that copy
    when the link points to an image."""
    soup = BeautifulSoup(html, "lxml")
    for img in soup.find_all("img"):
        src = (img.get("src") or "").strip()
        if not src.startswith("http"):
            continue
        best = src
        a = img.find_parent("a")
        href = (a.get("href") or "").strip() if a else ""
        if href and (re.search(r"\.(jpe?g|png|gif)$", href, re.I)
                     or "googleusercontent.com" in href
                     or "bp.blogspot.com" in href):
            best = href
        yield src, best


def fetch_images():
    IMAGES_DIR.mkdir(exist_ok=True)
    manifest = json.loads(IMAGE_MANIFEST.read_text()) if IMAGE_MANIFEST.exists() else {}
    failed = 0
    for post in load_entries():
        stem = f"{post['published']:%Y%m%d}-{slug_from_url(post['url'])}"
        for i, (src, best) in enumerate(image_sources(post["html"]), 1):
            if src in manifest and (IMAGES_DIR / manifest[src]).exists():
                continue
            data = ctype = None
            for url in dict.fromkeys([best, src]):      # fall back to src
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=60) as r:
                        data, ctype = r.read(), r.headers.get_content_type()
                    break
                except Exception as err:
                    print(f"  failed {url}: {err}")
            if data is None:
                failed += 1
                continue
            ext = {"image/jpeg": ".jpg", "image/png": ".png",
                   "image/gif": ".gif"}.get(ctype) or Path(urlparse(best).path).suffix.lower() or ".jpg"
            name = f"{stem}-{i}{ext}"
            (IMAGES_DIR / name).write_bytes(data)
            manifest[src] = name
            print(f"saved {name}")
    IMAGE_MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
    print(f"{len(manifest)} images saved, {failed} failed")


def load_entries():
    entries = []
    for f in sorted(FEED_DIR.glob("page-*.json")):
        entries += json.loads(f.read_text())["feed"].get("entry", [])
    posts = []
    for e in entries:
        link = next((l["href"] for l in e["link"] if l["rel"] == "alternate"), None)
        if link is None:  # drafts or link-less entries
            continue
        published = datetime.fromisoformat(e["published"]["$t"])
        posts.append({
            "title": e["title"]["$t"].strip() or "(untitled)",
            "published": published,
            "url": link,
            "labels": sorted(c["term"] for c in e.get("category", [])),
            "html": e.get("content", e.get("summary", {})).get("$t", ""),
        })
    posts.sort(key=lambda p: p["published"], reverse=True)
    return posts


# ---------------------------------------------------------------- converting

class FootnoteConverter(MarkdownConverter):
    """markdownify converter that turns <a href> into footnotes."""

    def __init__(self, images=None, **options):
        super().__init__(**options)
        self.notes = []          # list of URLs, footnote n = index + 1
        self.images = images or {}

    def note_for(self, href):
        # Re-use the same number if a post links to the same URL twice.
        if href in self.notes:
            return self.notes.index(href) + 1
        self.notes.append(href)
        return len(self.notes)

    def convert_a(self, el, text, *args, **kwargs):
        href = (el.get("href") or "").strip()
        if not href or href.startswith("#") or href.lower().startswith("javascript:"):
            return text
        # A link wrapped around a picture (Blogger does this for every image):
        # keep the picture, drop the link to the full-size copy.
        if el.find("img") and not el.get_text(strip=True):
            return text
        n = self.note_for(href)
        if not text.strip():
            return f"[^{n}]"
        return f"{text}[^{n}]"

    def convert_img(self, el, text, *args, **kwargs):
        src = (el.get("src") or "").strip()
        alt = (el.get("alt") or "").replace("]", "")
        if src in self.images:
            src = "../images/" + self.images[src]
        return f"![{alt}]({src})"

    def convert_code(self, el, text, *args, **kwargs):
        # Blogger posts put code on its own lines as <br><code>..</code>.
        # Code with line breaks becomes a fenced block; short snippets
        # stay inline.
        if not el.find("br") and "\n" not in el.get_text().strip():
            return super().convert_code(el, text, *args, **kwargs)
        return fenced(code_text(el), guess_language(code_text(el)))

    def convert_blockquote(self, el, text, *args, **kwargs):
        # Program output (Python lists, tuples, XML) was shown in quotes.
        raw = code_text(el)
        if looks_like_output(raw):
            return fenced(raw, "xml" if raw.lstrip().startswith("<") else "")
        return super().convert_blockquote(el, text, *args, **kwargs)


def code_text(el):
    """The literal text of an element, with <br> as line breaks."""
    el = BeautifulSoup(str(el), "lxml").find(el.name)
    for br in el.find_all("br"):
        br.replace_with("\n")
    lines = el.get_text().replace("\xa0", " ").split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(l.rstrip() for l in lines)


def guess_language(code):
    first = code.lstrip()
    if first.startswith("<"):
        return "html"
    if "{%" in code or re.fullmatch(r"https?://\S+", first.strip()):
        return ""
    if re.match(r"(\$ |wget |curl |cat |grep |sed |cd |ls |sort |for \w+ in .*; do)", first):
        return "bash"
    return "python"


def looks_like_output(text):
    return bool(re.match(r"\s*(\[|\(\d|'|\"\d|<\w)", text))


def fenced(code, lang):
    return f"\n\n```{lang}\n{code}\n```\n\n"


def slug_from_url(url):
    name = Path(urlparse(url).path).stem          # e.g. "my-first-post"
    name = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return name or "post"


def protect_liquid(md):
    """Stop GitHub Pages (Jekyll) from interpreting {{ }} or {% %} in posts."""
    if "{{" in md or "{%" in md:
        return "{% raw %}\n" + md + "\n{% endraw %}"
    return md


def escape_pipes(md):
    """Escape | outside `code` spans so kramdown doesn't build tables
    (Blogger posts end with lines like "Tags: a | b"). Table rows are left alone."""
    def fix(line):
        if line.lstrip().startswith("|"):      # a real table row
            return line
        parts = re.split(r"(`+[^`]*`+)", line)
        return "".join(p if p.startswith("`") else p.replace("|", "\\|")
                       for p in parts)
    out, in_fence = [], False
    for line in md.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
        out.append(line if in_fence or line.startswith("```") else fix(line))
    return "\n".join(out)


def convert(post, images=None):
    soup = BeautifulSoup(post["html"], "lxml")
    conv = FootnoteConverter(images=images, heading_style="ATX", bullets="*",
                             escape_underscores=True, escape_asterisks=True)
    body = conv.convert_soup(soup)
    body = re.sub(r"[ \t]+\n", lambda m: "  \n" if m.group(0).startswith("  ") else "\n", body)
    body = re.sub(r"\n[ \t]+(?=\n)", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    body = escape_pipes(body)
    return body, conv.notes


def md_text(s):
    """Escape a plain-text string (e.g. a title) for use in Markdown."""
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("[", "\\[").replace("]", "\\]"))


def nav_link(label, other):
    if other is None:
        return None
    p, fname = other
    return f"{label}: [{md_text(p['title'])}]({fname})"


def write_post(post, filename, older=None, newer=None, images=None):
    body, notes = convert(post, images)
    date = post["published"]
    meta = [f"_{date:%B} {date.day}, {date:%Y}_"]
    if post["labels"]:
        meta.append("_Labels: " + ", ".join(post["labels"]) + "_")
    meta.append(f"Originally published at `{post['url']}`")
    lines = [
        f"# {md_text(post['title'])}",
        "",
        "  \n".join(meta),
        "",
        protect_liquid(body),
        "",
        "---",
        "",
    ]
    nav = [x for x in (nav_link("Previous", older), nav_link("Next", newer)) if x]
    nav.append("[Back to the blog archive](../README.md)")
    lines += ["  \n".join(nav), ""]
    # kramdown (used by GitHub Pages) always prints footnotes at the very
    # bottom of the page, after a horizontal rule.
    lines += [f"[^{i}]: `{url}`" for i, url in enumerate(notes, 1)]
    (POSTS_DIR / filename).write_text("\n".join(lines).rstrip() + "\n")


def build():
    posts = load_entries()
    POSTS_DIR.mkdir(exist_ok=True)
    for old in POSTS_DIR.glob("*.md"):
        old.unlink()
    images = json.loads(IMAGE_MANIFEST.read_text()) if IMAGE_MANIFEST.exists() else {}
    used = set()
    index = []
    for p in posts:
        name = f"{p['published']:%Y%m%d}-{slug_from_url(p['url'])}"
        base, k = name, 2
        while name in used:
            name, k = f"{base}-{k}", k + 1
        used.add(name)
        index.append((p, name + ".md"))
    # index is newest first: the "next" post is newer, "previous" is older.
    for i, (p, fname) in enumerate(index):
        newer = index[i - 1] if i > 0 else None
        older = index[i + 1] if i + 1 < len(index) else None
        write_post(p, fname, older, newer, images)

    # The last post (2011) is just a pointer to GitHub, so the blog's
    # active years are given by hand.
    first, last = 2005, 2008
    out = [
        "# Digital History Hacks",
        "",
        f"From {first} to {last} I kept a blog called _Digital History Hacks_ at "
        f"`{BLOG}/`. This page archives all {len(posts)} posts, "
        "newest first. Each post has been converted to Markdown, and its "
        "hyperlinks are given as numbered footnotes showing the original URL "
        "(many of which no longer work).",
        "",
        "[Back to the home page](../README.md)",
        "",
    ]
    year = None
    for p, fname in index:
        y = p["published"].year
        if y != year:
            out += ["", f"## {y}", ""]
            year = y
        d = p["published"]
        title = md_text(p["title"])
        out.append(f"* {d:%b} {d.day} &middot; [{title}](posts/{fname})")
    out.append("")
    (BLOG_DIR / "README.md").write_text("\n".join(out))
    print(f"wrote {len(posts)} posts")


if __name__ == "__main__":
    {"fetch": fetch, "images": fetch_images, "build": build}[sys.argv[1] if len(sys.argv) > 1 else "build"]()
