#!/usr/bin/env python3
"""Build the Digital History Hacks archive from the Blogger feed.

Usage:
    python3 blog/_tools/build_blog_archive.py fetch   # download feed JSON to blog/_tools/feed/
    python3 blog/_tools/build_blog_archive.py build   # write blog/posts/*.md and blog/README.md

Each post becomes blog/posts/YYYYMMDD-slug.md. Every hyperlink in a post is
replaced by a numbered Markdown footnote, and the footnote shows the original
URL as plain text. Images are kept as images.

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

    def __init__(self, **options):
        super().__init__(**options)
        self.notes = []          # list of URLs, footnote n = index + 1

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


def slug_from_url(url):
    name = Path(urlparse(url).path).stem          # e.g. "my-first-post"
    name = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return name or "post"


def protect_liquid(md):
    """Stop GitHub Pages (Jekyll) from interpreting {{ }} or {% %} in posts."""
    if "{{" in md or "{%" in md:
        return "{% raw %}\n" + md + "\n{% endraw %}"
    return md


def convert(post):
    soup = BeautifulSoup(post["html"], "lxml")
    conv = FootnoteConverter(heading_style="ATX", bullets="*",
                             escape_underscores=True, escape_asterisks=True)
    body = conv.convert_soup(soup)
    body = re.sub(r"[ \t]+\n", lambda m: "  \n" if m.group(0).startswith("  ") else "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body, conv.notes


def md_text(s):
    """Escape a plain-text string (e.g. a title) for use in Markdown."""
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("[", "\\[").replace("]", "\\]"))


def write_post(post, filename):
    body, notes = convert(post)
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
        "[Back to the blog archive](../README.md)",
        "",
    ]
    # kramdown (used by GitHub Pages) always prints footnotes at the very
    # bottom of the page, after a horizontal rule.
    lines += [f"[^{i}]: `{url}`" for i, url in enumerate(notes, 1)]
    (POSTS_DIR / filename).write_text("\n".join(lines).rstrip() + "\n")


def build():
    posts = load_entries()
    POSTS_DIR.mkdir(exist_ok=True)
    for old in POSTS_DIR.glob("*.md"):
        old.unlink()
    used = set()
    index = []
    for p in posts:
        name = f"{p['published']:%Y%m%d}-{slug_from_url(p['url'])}"
        base, k = name, 2
        while name in used:
            name, k = f"{base}-{k}", k + 1
        used.add(name)
        write_post(p, name + ".md")
        index.append((p, name + ".md"))

    first, last = posts[-1]["published"].year, posts[0]["published"].year
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
    {"fetch": fetch, "build": build}[sys.argv[1] if len(sys.argv) > 1 else "build"]()
