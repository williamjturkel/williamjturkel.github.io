# Working in the Browser

_July 24, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/07/working-in-browser.html`

Working with digital sources means that historians will spend more time working with computers. Most already use e-mail and word processing, search library catalogs and archival finding aids, read online journal articles and book reviews. Digital history puts primary and secondary sources onto the computer, too, and provides new opportunities for historical research and writing: blogging, digitization, web and wiki authoring, programming, and so on. With the shift toward Web 2.0[^1], more and more of these activities can be done in the browser. You can work anywhere that you have a computer and an internet connection, and all of your notes and files can be stored on a server somewhere else. (For an exploration of some of the possibilities, see James Fallows' article "Homo Conexus[^2]" in the new issue of Tech Review.)  
  
Until relatively recently, however, writing and citing have been done from within standalone applications like Microsoft Word and Endnote. In order to work on your book or article, you've had to have the applications installed on the computer that you're using. If you want to work on another machine, you need the programs installed on that machine, too. Depending on the software licenses involved, you might need to buy new copies of application software for every machine you want to work on. And, of course, you have to make sure that your files are synchronized across all of your machines, or, at the very least, that you are editing the latest version of each.  
  
Researchers at the Center for History and New Media at George Mason University are working to change this paradigm by creating a tool they call Firefox Scholar[^3]. Built on top of the popular browser Firefox, the Scholar extensions "will allow researchers to recognize and capture metadata from online objects; collect documents, images, and citations from the web; and allow those materials to be sorted, annotated, and searched--all directly within their web browser window." That's pretty sweet. Best of all, it will be possible for scholar-hackers to extend the system themselves, and build new functionality into it. As Dan Cohen noted[^4] a few days ago in his blog, the beta version will be coming soon, and CHNM is still looking for people to test it.  
  
Now that I have a working server[^5] set up, I've decided to take a page from Firefox Scholar and try building some data mining and visualization tools into the browser as extensions. My hope is that some of these may eventually find their way into Scholar, but in the meantime I'll learn some new techniques and, hopefully, create some tools I can use in my own research.  
  
Putting work into the browser makes things easier for the user at the cost of increasing complexity for the programmer(s). Here's an overview of some of the components we will need to work with:  

* Firefox[^6], an extensible browser, uses Javascript[^7] and XUL[^8]
* Making things look good on the client side will require CSS[^9] and AJAX[^10]
* Making things work on the server side will require a database (MySQL[^11]), a scripting language (PHP[^12]), a search engine toolkit (Plucene[^13]) and maybe some other goodies (like Cake[^14])
* We'll also need custom-made or off-the-shelf mining and visualization components

Tags: browser[^15] \| citation[^16] \| data mining[^17] \| digital history[^18] \| hacking[^19] \| open source[^20] \| server[^21] \| web programming[^22]

[Back to the blog archive](../README.md)

[^1]: `http://www.oreillynet.com/pub/a/oreilly/tim/news/2005/09/30/what-is-web-20.html`
[^2]: `http://www.technologyreview.com/read_article.aspx?id=17061&ch=infotech`
[^3]: `http://chnm.gmu.edu/tools/firefoxscholar/`
[^4]: `http://www.dancohen.org/blog/posts/acls_fellowships_chicago_colloquium_scholar_update`
[^5]: `http://digitalhistory.uwo.ca`
[^6]: `http://www.mozilla.com/firefox/`
[^7]: `http://www.w3schools.com/js/default.asp`
[^8]: `http://www.mozilla.org/projects/xul/`
[^9]: `http://www.w3schools.com/css/default.asp`
[^10]: `http://www.w3schools.com/ajax/default.asp`
[^11]: `http://dev.mysql.com/`
[^12]: `http://www.w3schools.com/php/default.asp`
[^13]: `http://www.perl.com/pub/a/2004/02/19/plucene.html`
[^14]: `http://cakephp.org/`
[^15]: `http://technorati.com/tag/browser`
[^16]: `http://technorati.com/tag/citation`
[^17]: `http://technorati.com/tag/data+mining`
[^18]: `http://technorati.com/tag/digital+history`
[^19]: `http://technorati.com/tag/hacking`
[^20]: `http://technorati.com/tag/open+source`
[^21]: `http://technorati.com/tag/search`
[^22]: `http://technorati.com/tag/web+programming`
