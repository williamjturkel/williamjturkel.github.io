# Teaching Young Historians to Search, Spider and Scrape

_December 26, 2005_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2005/12/teaching-young-historians-to-search.html`

[A newer edition of this post is available here[^1]]  
  
A large part of learning to be a historian is learning new ways to read. Different kinds of sources require different kinds of readings. In graduate school, one learns that starting at the beginning of a book and plowing through to the end results in a single furrow: straight perhaps, but not particularly deep. In many PhD programs, the comprehensive (or qualifying) exams are the point when the student has to give up this kind of reading in order to master a large body of material in a short span of time. Comps are not only an important rite of passage; they also change us by changing the ways that we read. After I finished my comps, I discovered that I was no longer able to read fiction the way I had before. One colleague tells me that the process made him more introspective. Another became very discouraged by the thought that he would spend a decade writing a book that some other grad student would process in an hour and a half. Learning how to process a book in this fashion is crucial for history students, and I usually give beginners Paul Edwards' short guide "How to Read a Book[^2]."  
  
The ability to search for books online, and to search through them, has greatly changed the possible ways of reading available to historians, and yet the necessary skills are not yet being explicitly taught to students. Some follow from commercial applications. Take Amazon[^3] for example. It is straightforward to build a preliminary bibliography by starting with a given book in their database and following recommendations. People who have viewed (or bought) the book that you are interested in have also viewed or bought ones you might be interested in. In many cases, Amazon also lets you search for words or phrases within books, and view the covers, table of contents and index for the book. As Edwards notes, these are precisely the places where information about the book can be gathered most quickly.  
  
For some books, the Amazon database includes additional information, like SIPs: statistically improbable phrases. A SIP is a phrase that is common in the book that you are looking at, but that doesn't commonly appear in many other books. For Jared Diamond's Guns, Germs and Steel, for example, the SIPs include "blueprint copying," "mammal domestication," "founder crops," "intensified food production," "crowd diseases" and "dense human populations." Amazon lets you click on each SIP to see all of the uses of that phrase in context. Someone who hadn't read Diamond's book would still be able to learn a lot about it by studying its SIPs. Furthermore, each SIP connects Guns, Germs and Steel with the surrounding literature. "Founder crops" is also used by Zohary and Hopf in Domestication of Plants in the Old World; "intensified food production" by McMichael in Human Frontiers, Environments and Disease; and "dense human populations" by Wm. McNeill in Plagues and Peoples, Hays in Burdens of Disease, Flannery in The Future Eaters, and Melville in A Plague of Sheep. Someone who is familiar with the tools that Amazon provides can learn a lot about a particular literature without reading a single book. With a bit of programming, it is possible to do still more (see Paul Bausch's Amazon Hacks[^4] to get started).  
  
The idea of searching is familiar to historians, although many of the possibilities raised by search engines like Google[^5] and Yahoo![^6] are probably not. To get the most out of the web, however, it is crucial that we begin to teach history students the rudiments of web programming. Spidering, for example, is the (automated) process of visiting a webpage, creating an index and a list of links to further pages, and then following each of those in turn and doing the same thing. Whenever we follow the citations in a footnote to another source, and then begin to read its footnotes, we are doing a kind of spidering. By teaching students how to implement this process on the computer we will not only teach them a crucial skill, we will make them more aware of the technologies that have long underlain the historian's craft.  
  
Scraping refers to the process of mechanically extracting information from sources (like webpages) that are intended to be read by people rather than machines. Because computers don't understand text in the way that people do, scraping has to rely on the form of the text to extract information, rather than the meaning. As a result, scrapers are 'brittle': if the form changes, the scraper breaks. For this reason, it is important for historians to be able to create their own tools, rather than using the tools created by others, and this, again, means that it is necessary to learn some rudimentary web programming. (For more on spidering and scraping, see Kevin Hemenway and Tara Calishain's Spidering Hacks[^7].)  
  
For a new generation of digital historians, however, the payoff of learning to search, spider and scrape will lie not only in the ability to design and execute new kinds of historical project, but in the increased reflexive awareness that comes from writing programs to augment reading.  
  
Tags: digital history[^8] \| hacking[^9] \| pedagogy[^10] \| search[^11] \| SIPs[^12] \| spidering[^13] \| web programming[^14]

[Back to the blog archive](../README.md)

[^1]: `http://williamjturkel.net/digital-history-hacks-2005-08/2005-12-26-teaching-young-historians-to-search-spider-and-scrape/`
[^2]: `http://www.si.umich.edu/%7Epne/read.a.book.htm`
[^3]: `http://www.amazon.com/`
[^4]: `http://www.oreilly.com/catalog/amazonhks/`
[^5]: `http://www.google.com/`
[^6]: `http://www.yahoo.com/`
[^7]: `http://www.oreilly.com/catalog/spiderhks/`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/hacking`
[^10]: `http://technorati.com/tag/pedagogy`
[^11]: `http://technorati.com/tag/search`
[^12]: `http://technorati.com/tag/sips`
[^13]: `http://technorati.com/tag/spidering`
[^14]: `http://technorati.com/tag/web+programming`
