# Easy Pieces in Python: Simple Scraping

_September 3, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/09/easy-pieces-in-python-simple-scraping.html`

Information on the web is increasingly made available in forms that are easy for machines to process, often variants of XML[^1]. Many sites, however, still present information in a way that looks good to human readers but is more difficult to process automatically. In cases like these, it is nice to be able to write a scraper[^2] to extract the information of interest.  
  
As an example, suppose we are working with OCLC's fabulous new Open WorldCat[^3], which allows web users to search the catalogs of over 10,000 different libraries with a single search. Among other things, the system allows the user to find all of the different works created by an author and to locate copies of any given work. Open WorldCat is designed for human searchers, however, so you have to do a bit of programming if you want to automatically extract information from their pages.  
  
Most scraping starts with the programmer looking at the webpage of interest and comparing it with the code that generated it. You can do this in Firefox[^4] by going to the page and choosing View -- Page Source (in Internet Explorer the command is View -- Source). The basic idea is to locate instances of the information that you are interested in and study the context of these in the code. Is there something that always precedes or follows the thing you are interested in? If so, you can write a regular expression[^5] to match that context.  
  
Suppose we are looking for works by a particular author, say Alan MacEachern[^6]. The WorldCat URLs for his author page, for a particular book (The Institute of Man and Resources[^7]), and for all copies of that book in Ontario are shown below. Since we are programming in Python[^8], we assign them to variables.  
 `authorurl = r'http://www.worldcat.org/search?q=alan+maceachern'  
workurl = r'http://www.worldcat.org/oclc/51839396'  
locationurl = r'http://www.worldcat.org/oclc/51839396&tab=holdings?loc=ontario#tabs'`  
Having studied the source code of those pages, we've also determined the patterns that we will need to extract works from the author page and library addresses from the location pages. (I admit that I'm reaching a bit when I call this part "easy"... I guess it is easy if you already know how to use regular expressions. Hang in there.)  
 `workpattern = '<a.*?href="/oclc/(.*?)\&.*?".*?>.*?</a>'  
addresspattern = r'<td class="location">(.*?)</td>'`  
Now we need some code that will open a webpage, pass our pattern across it line by line, and return any matches. Since we will want to reuse this code whenever we need to scrape a page, we wrap it in a function.  
 `import re, urllib  
def scraper(url, filter=r'.*'):  
  page = urllib.urlopen(url)  
  pattern = re.compile(filter, re.IGNORECASE)  
  returnlist = []  
  for line in page.readlines():  
    returnlist += pattern.findall(line)  
  return returnlist`  
So, how does it work? We can now ask it to return the OCLC numbers for all works created by Alan MacEachern:  
 `r = scraper(authorurl, workpattern)  
print r`  
And this is what we get:  
> ['44713451', '51839396', '61175031', '40538595', '46521636']

  
And we can ask it to return the addresses of all of the libraries in Ontario that have a copy of *The Institute of Man and Natural Resources*:  
 `r = scraper(locationurl, addresspattern)  
print r`  
And this is what we get:  
> ['Waterloo, ON N2L 3C5 Canada', 'Ottawa, ON K1A 0N4 Canada', 'Hamilton, ON L8S 4L6 Canada', 'Kingston, ON K7L 5C4 Canada', 'Toronto, ON M5B 2K3 Canada', 'Guelph, ON N1G 2W1 Canada', 'London, ON N6A 3K7 Canada']

  
By modifying the URLs and patterns that we feed into our scraper, we can accomplish a wide variety of scraping tasks with a small amount of code.  
  
Tags: hacking[^9] | python[^10] | scraping[^11] | WorldCat[^12] | XML[^13]

[Back to the blog archive](../README.md)

[^1]: `http://www.w3schools.com/xml/`
[^2]: `http://en.wikipedia.org/wiki/Screen_scraping`
[^3]: `http://www.worldcat.org`
[^4]: `http://www.mozilla.com/firefox/`
[^5]: `http://www.amazon.com/dp/0596528124/`
[^6]: `http://alanmaceachern.blogspot.com`
[^7]: `http://www.amazon.com/dp/0919013376`
[^8]: `http://www.python.org`
[^9]: `http://technorati.com/tag/hacking`
[^10]: `http://technorati.com/tag/python`
[^11]: `http://technorati.com/tag/scraping`
[^12]: `http://technorati.com/tag/worldcat`
[^13]: `http://technorati.com/tag/xml`
