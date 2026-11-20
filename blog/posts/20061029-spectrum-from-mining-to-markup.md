# The Spectrum from Mining to Markup

_October 29, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/10/spectrum-from-mining-to-markup.html`

In a series of earlier posts[^1] I've shown that simple text and data mining techniques can be used to extract information from a sample historical source, the online Dictionary of Canadian Biography[^2]. With such techniques it is possible to cluster related biographies, to try to determine overall themes or to extract items of information like names, dates and places. Information extraction can be particularly tricky because natural languages are ambiguous. In the DCB, for example, 'Mary' might be a person's name, the name of a ship or the Virgin Mary; 'Champlain' might be the person or any number of geographical features named for him. To some extent these can be disambiguated by clever use of context: 'the Mary' is probably a ship, 'Lake Champlain' is a place (although in a phrase like 'the lake Champlain visited' the word 'Champlain' refers to the person), and so on.  

In order to make information explicit in electronic texts, human analysts can add a layer of markup. These tags can then be used to automate processing. I've recently begun a project to tag names and dates in Volume 1 of the DCB using the Text Encoding Initiative[^3] XML-based standard TEI Lite[^4]. These tags explicitly disambiguate different uses of the same word  

his wife **<name type="person" reg="Abraham, Mary">**Mary**</name>**  
versus  
boarded the **<name type="ship">**Mary**</name>**  

the lake **<name type="person" key="34237" reg="Champlain, Samuel de">**Champlain**</name>** visited  
versus  
visited **<name type="place">**Lake Champlain**</name>**  

Tags can also be used to add information that is clear to the reader but would be missed during machine processing. When the biography of John Abraham refers to his wife Mary, the person marking up the text can add the information that the person meant is "Abraham, Mary" and not, say, "Silver, Mary." In the case of someone like Champlain who has a biography in the DCB, the person's unique identifier can also be added to the tag. The information that is added in tags can be particularly valuable when marking up dates, as shown below.  

**<date value="1690">**1690**</date>**  
**<date value="1690-09">**September of the same year**</date>**  
**<date value="1690-09-12">**twelfth of the month**</date>**  
**<date value="1690-06/1690-08" certainty="approx">**summer of 1690**</date>**  

In a later pass, my research assistants and I will add latitude and longitude to place name tags. For now, we are concentrating on clarifying dates and disambiguating proper nouns. So we are tagging the names of people ('Champlain'), places ('Lake Champlain'), ships ('the Diligence'), events ('third Anglo-Dutch War'), institutions ('Hudson's Bay Company'), ethnonyms ('the French') and others.  

Given texts marked up this way, the next step is to write programs that can make use of the tags. In the Python Cookbook[^5], Paul Prescod writes  
> Python and XML are perfect complements. XML is an open standards way of exchanging information. Python is an open source language that processes the information. Python excels at text processing and at handling complicated data structures. XML is text based and is, above all, a way of exchanging complicated data structures.

In future posts, I will introduce some of the python code that we are using to process the marked up DCB entries. In the meantime I can suggest a few of the many different kinds of questions that can be answered with these texts:  

* Are discussions of particular ethnic groups limited to ranges of time? Do Basques, for example, play a walk-on part in the early cod fishery only to more-or-less disappear from the story of Canadian history after that?

* If you start with a particular person and link to all of the people mentioned in his or her biography, and then link to all of the people mentioned in theirs, do you eventually connect to everyone in Volume 1? In other words, is it a small world[^6]?

* If you start with a particular place and time (say Trois-Rivières in 1660) and search for all of the events that happened in the preceding decade within a 50km radius, are they related? If so, how?

The classicist and digital humanist Gregory Crane has recently written that "Already the books in a digital library are beginning to read one another and to confer among themselves before creating a new synthetic document for review by their human readers" [What Do You Do with a Million Books?[^7]] This magic is accomplished, in part, by markup. If the system knows which 'Mary' is meant in a particular text it is quite easy to provide links to the same person (or saint, or ship) in other documents in the same digital collection. At the moment we are adding these links by hand, but it is easy to imagine building a system that uses text mining to assign preliminary tags, allows a human analyst to provide correction, then uses that feedback to learn. The Gamera project[^8] already provides a framework like this for doing OCR[^9] on texts of historical interest.  

Tags: data mining[^10] \| dictionary of canadian biography[^11] \| link analysis[^12] \| python[^13] \| tagging[^14] \| text encoding initiative[^15] \| text mining[^16] \| xml[^17]

---

Previous: [Behind the Scenes of a Digital History Site](20061015-behind-scenes-of-digital-history-site.md)  
Next: [Wikis and Philological Criticism](20061109-wikis-and-philological-criticism.md)  
[Back to the blog archive](../README.md)

[^1]: `http://search.blogger.com/?as_q=dcb&ie=UTF-8&ui=blg&bl_url=digitalhistoryhacks.blogspot.com`
[^2]: `http://www.biographi.ca/EN`
[^3]: `http://www.tei-c.org/`
[^4]: `http://www.tei-c.org/Lite/teiu5_split_en.html`
[^5]: `http://www.amazon.com/Python-Cookbook-Alex-Martelli/dp/0596007973/`
[^6]: `http://en.wikipedia.org/wiki/Small_world_phenomenon`
[^7]: `http://www.dlib.org/dlib/march06/crane/03crane.html`
[^8]: `http://ldp.library.jhu.edu/projects/gamera/`
[^9]: `http://en.wikipedia.org/wiki/Optical_character_recognition`
[^10]: `http://technorati.com/tag/data+mining`
[^11]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^12]: `http://technorati.com/tag/link+analysis`
[^13]: `http://technorati.com/tag/python`
[^14]: `http://technorati.com/tag/tagging`
[^15]: `http://technorati.com/tag/text+encoding+initiative`
[^16]: `http://technorati.com/tag/text+mining`
[^17]: `http://technorati.com/tag/xml`
