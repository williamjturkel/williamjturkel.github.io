# Text Mining the DCB, Part 5

_February 19, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/02/text-mining-dcb-part-5.html`

My original plan for this series of posts was to show how it is relatively simple to spider an online historical collection like the Dictionary of Canadian Biography[^1], scrape out some information, and use it to make possibly novel inferences. Up until now, we've been storing information in text files, which is OK for a simple demo but unwieldy if we want to try something more ambitious.  

As a result I've decided to make a few modifications so that we can store information in a relational database[^2] instead. Eventually, I will probably implement something open source on a server, like MySQL[^3]. In the meantime, however, I already have MS Access[^4] installed on my computer so that is what I am going to use. It shouldn't be too hard to port[^5] later.  

In my next post I will describe the intial data tables and the way we get Perl to talk to our database...  

Tags: dictionary of canadian biography[^6] \| digital history[^7] \| relational databases[^8] \| text mining[^9]

---

Previous: [Historiographical Process(ing)](20060210-historiographical-processing.md)  
Next: [Brief Hiatus](20060301-brief-hiatus.md)  
[Back to the blog archive](../README.md)

[^1]: `http://www.biographi.ca/EN`
[^2]: `http://en.wikipedia.org/wiki/Relational_databases`
[^3]: `http://www.mysql.com/`
[^4]: `http://office.microsoft.com/en-us/FX010857911033.aspx`
[^5]: `http://en.wikipedia.org/wiki/Porting`
[^6]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^7]: `http://technorati.com/tag/digital+history`
[^8]: `http://technorati.com/tag/relational+databases`
[^9]: `http://technorati.com/tag/text+mining`
