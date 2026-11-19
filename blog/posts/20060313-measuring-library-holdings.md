# Measuring Library Holdings

_March 13, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/03/measuring-library-holdings.html`

Most professors get paid for some agreed-upon mix of research, teaching and service. I've spent most of my time in this blog making a case for the ways that web programming can and will change the research and teaching of history. This week, however, I had the unexpected pleasure of doing a little service-related hacking.  

Like every graduate program in the province, our department[^1] is subject to periodic review by the Ontario Council on Graduate Studies[^2]. One of the things that we thought might be useful was to try to find ways to assess the suitability of our library holdings for various kinds of historical projects. My colleague Allyson May[^3] had the good idea of checking books reviewed on various H-Net lists against our library holdings. Unlike regular journals, H-Net reviews tend to come out much more quickly, and thus are a better measure of recent literature of interest to historians. Of course, there are 170 H-Net discussion lists[^4], some defunct, some with hundreds of book reviews over the last 13 years, and some with none. If you think this doesn't sound like something you'd want to do by hand[^5], you're right.  

In the following two hacks we automate the process. First[^6], we go to the page of H-Net lists and get the name of each discussion list. The we go to the review search page, and, one-by-one, we search for all of the book reviews published on each discussion list. We save the links to each individual book review. We then spider the reviews, scrape the ISBN out of each, and save it to a file. Then[^7], we submit each of the ISBNs to our library catalogue, and do a bit of rudimentary scraping to see if each book is in the library or not. Finally, we can accumulate the final results in a spreadsheet for whatever further analysis is required.  

Tags: bibliography[^8] \| hacking[^9] \| h-net[^10] \| spidering[^11] \| web programming[^12]

---

Previous: [Blogospheric Stock](20060310-blogospheric-stock.md)  
Next: [Compression](20060319-compression.md)  
[Back to the blog archive](../README.md)

[^1]: `http://history.uwo.ca/`
[^2]: `http://ocgs.cou.on.ca/`
[^3]: `http://history.uwo.ca/faculty/may/`
[^4]: `http://www.h-net.org/lists/`
[^5]: `http://en.wikipedia.org/wiki/Sysiphus`
[^6]: `http://digitalhistory.uwo.ca/dhh/hacks/h-reviews.pl.html`
[^7]: `http://digitalhistory.uwo.ca/dhh/hacks/h-rev-catalogue.pl.html`
[^8]: `http://technorati.com/tag/bibliography`
[^9]: `http://technorati.com/tag/hacking`
[^10]: `http://technorati.com/tag/h-net`
[^11]: `http://technorati.com/tag/spidering`
[^12]: `http://technorati.com/tag/web+programming`
