# A First Look at Zotero

_September 7, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/09/first-look-at-zotero.html`

Our school year officially started today but I'm not teaching on Thursdays this term, so I was able to spend the day hacking the pre-release beta of Zotero[^1] and listening to an album of pioneering[^2] electronic music. The music turned out to be the perfect complement to the software.  
  
The basics. Zotero is the brainchild of a team of digital historians at the Center for History and New Media[^3] at George Mason University: Dan Cohen[^4], Josh Greenberg[^5], Simon Kornblith[^6], David Norton and Dan Stillman. Their basic goal was to create a freely available, open source tool that would put the essential functions of standalone bibliography software like Endnote into the Firefox[^7] browser. Since we already spend most of the day reading and writing in our browsers (e-mail, blogging, newsfeeds, online journals, e-books, library catalogs, etc.) this makes a lot of sense. Like commercially available packages, Zotero allows you to create and cite from a database of primary and secondary references of various types (books, newspaper articles, journal articles, and so on). Instead of starting a separate program, however, you can enter records as you browse library catalogs (e.g., Library of Congress, WorldCat), bookstores (Amazon.com) and many other websites.  
  
Zotero already has some distinct advantages over commercial bibliographic management software. For one thing, you can arrange your sources hierarchically. The interface is divided into three panels which give you different views into your collections of sources, using the familiar file folder metaphor. The lefthand panel shows a top level view of folders, the centre panel shows the contents of the currently selected folder, and the righthand panel shows a tabbed display of the details for the currently selected item. You can see a screenshot of the interface in the quick start guide[^8]. It is easy to customize the information presented in the middle panel. Zotero not only allows you to create bibliographic records, but also makes it easy to link to webpages, to snapshots of webpages, to other files like JPEGs and PDFs, and to notes which you can create directly in your browser. You can tag records with Library of Congress subject headings (LCSH) or with your own tags, or a mixture of the two. You can also link records within your collections to one another. (I have to admit that I haven't quite figured out a use for this.) The interface also easily toggles between views that take up all, some or none of the browser page. Finally, there is a feature called "smart collections" which lets you save the results of a search as a virtual folder. This is handy because it gives you different views of the same data without requiring you to enter it in multiple places.  
  
Sensing citation information. Let's take it as read that Zotero is a great tool for keeping track of your bibliographical information without leaving the browser. But there's more. When you browse a page that has citation information embedded in it, Zotero "senses" that and lets you know. You then have the option of automatically scraping some or all of the data to your bibliographic database. The beta version already supports this behaviour at a number of widely used sites[^9] like the Library of Congress, WorldCat, Amazon.com and the New York Times. In my trial runs, it worked perfectly at the Library of Congress and Amazon, and with a few hiccups at a number of other sites. Since Zotero is extensible, expect to see user-contributed scrapers start to appear as soon as the beta is released. (More on this below). In my own university's library catalog, I had to switch to MARC[^10] view, and then Zotero worked perfectly. But then scrapers are notoriously brittle.  
  
Hacking Zotero. Zotero exports to RDF/XML[^11] and imports from a number of XML-based standards (RDF, MARC, MODS[^12] and RIS). Since it is pretty easy to write programs to manipulate RDF/XML in high-level programming languages, it will be possible for digital historians to collect resources via browsing in Zotero, then automate the processing of those records. It will also be possible to write programs that collect raw data (e.g., spiders), do some processing and then write the output in a format that can be imported into Zotero and scanned by a human interpreter. In other words, your Zotero collection (or anyone else's, or a whole bunch of people's) can be part of a workflow that includes both people and machines. This will be very useful for text and data mining projects.  
  
Behind the scenes. (This part of the review can be safely skipped if you aren't going to modify the program yourself). Since Zotero is open source, it is possible to look at the code and see how it works. Then hack it. Zotero installs two folders in your Firefox profile[^13], one called "zotero" that holds your data, and one called "extensions/zotero@chnm.gmu.edu" that holds the source code. The former contains a SQLite[^14] database that Firefox (and thus Zotero) uses to hold client-side information. You can download a SQLite utility that allows you to interact with the tables WHEN YOU ARE NOT RUNNING FIREFOX. (Otherwise you run the risk of hosing your database.) With this utility you can enter commands like ".schema" to see the SQL statements needed to create the database, or "select \* from tags" which shows you the tags you have already created. Modifications to the Zotero code can be done in a few places, notably the files "schema.sql" and "scrapers.sql". If you wanted to add record types to your database, for example, you'd have to modify the former. The scrapers are written in JavaScript[^15] and stored in the database. Presumably, the stable release of Zotero will include some tutorials showing how to write simple scrapers, but an intrepid programmer can probably figure it out from the supplied code. (And more. You can almost feel Kornblith's pain in one of his plaintive comments: "// Why can''t amazon use the same stylesheets".)  
  
Notes for the Zotero team. Don't let my suggestions for future improvements distract you from the bottom line: Zotero is already an amazing piece of software that could change the way we do history. The visionary team at CHNM should really be congratulated for making this, and making it open source. But since it is a beta release...  

* There is a time stamp when records are added to the database or modified, which is great. The same information isn't readily available, however, when one takes a snapshot of a webpage.
* Library of Congress scraper: want to automatically harvest links like URLs. Future releases (or hacks) could build on this by including the ability to spider within Zotero.
* WorldCat scraper: should grab OCLC number and put it into call number field. Again, this is crucial for automated spidering.
* Geocoding: please, please add fields for latitude and longitude. Geocoded sources are worth having, and I want to mash them up with the Google Maps API[^16] and MapServer[^17].
* Record types: at the very least, we need a generic record type to hold odds and ends. Ideally there would also be new types for blogs, blog posts, archival fonds, generic material objects and audio cds.
* Tags: when adding tags, should have a lookup table so you can select one that you've already used (good for consistency).
* Tags: nice to have a way of browsing by tag (as in del.icio.us), probably over in the lefthand panel.
* RSS feeds: it would be awesome if the functionality of Sage[^18] was built into the lefthand pane. Many of the sources I want to cite these days are blog posts.

  
Tags: hacking[^19] | zotero[^20]

[Back to the blog archive](../README.md)

[^1]: `http://www.zotero.org/`
[^2]: `http://www.amazon.com/Ohm-Gurus-Electronic-Music-Special/dp/B000BDGVX6`
[^3]: `http://chnm.gmu.edu/`
[^4]: `http://www.dancohen.org/`
[^5]: `http://www.epistemographer.com/`
[^6]: `http://simonster.com/`
[^7]: `http://www.mozilla.com/firefox/`
[^8]: `http://www.zotero.org/docs/quick_start_guide`
[^9]: `http://www.zotero.org/docs/sites.php`
[^10]: `http://www.loc.gov/marc/`
[^11]: `http://www.xml.com/pub/a/2001/01/24/rdf.html`
[^12]: `http://www.loc.gov/standards/mods//`
[^13]: `http://www.mozilla.org/support/firefox/profile#locate`
[^14]: `http://www.sqlite.org/`
[^15]: `http://www.w3schools.com/js/default.asp`
[^16]: `http://www.google.com/apis/maps/`
[^17]: `http://mapserver.gis.umn.edu/`
[^18]: `http://sage.mozdev.org/`
[^19]: `http://technorati.com/tag/hacking`
[^20]: `http://technorati.com/tag/zotero`
