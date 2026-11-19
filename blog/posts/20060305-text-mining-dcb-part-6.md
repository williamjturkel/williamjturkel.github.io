# Text Mining the DCB, Part 6

_March 5, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/03/text-mining-dcb-part-6.html`

In my last update[^1] on this project I said that I was in the process of moving the Dictionary of Canadian Biography[^2] stuff to a relational database to allow more sophisticated mining. At this point it is worth sketching out some of the kinds of things that we would like the system to do, and how that affects the design of the database tables.  

Imagine for a moment that we wanted to find more information relating to a particular figure in Early Canada, such as Médard Chouart Des Groseilliers[^3], known to Canadian schoolchildren as "Gooseberry" ... or at least to those who remember their history. Anyway, we could type 'groseilliers' into Google[^4] and see what we get. As of this moment, there are 46,700 hits. The first 10 are all relevant, coming from Collections Canada[^5], a PBS series on the HBC[^6], various encyclopedias and so on. If we were looking for information related to Des Groseilliers's companion Pierre-Esprit Radisson[^7], a comparable search[^8] now turns up fourteen and a half million hits. The first twenty hits are all related to the Radisson hotel chain. In fact, the Radisson Hotel in Kathmandu (someplace I've never been, incidently) receives a higher billing in the search results than our lowly explorer. Both "Groseilliers" and "Radisson" are relatively distinctive names, however. What if we were interested in someone like John Abraham[^9] (fl 1672-89), governor of Port Nelson? Since both "John" and "Abraham" are common names, and since both can serve as either personal name or surname, we know that a Google search is probably going to be more-or-less useless (and in fact returns 21.5 million hits).  

We'd obviously like to be able to pull needles like John Abraham out of the haystack, and this is where data mining comes in. One branch of the discipline concentrates on a group of related techniques known variously as link analysis, social network analysis and graph mining. (Papers from past SIAM[^10] conferences on data mining are a nice source of information, available online[^11].) The basic idea is fairly straightforward. We know that the John Abraham that we are interested in lived in the late 17th century, operated in a variety of locations around Hudson Bay, and knew various other individuals like Charles Bayly[^12], John Nixon[^13], Nehemiah Walker[^14], John-Baptiste Chouart, George Geyer[^15] and others. We know that he was mate of the Diligence in 1681, captain of the George and that he helped capture the Expectation in 1683. If we bring in some of this additional information, we might be able to refine our search to the point where it yields something interesting. If we Google for "+john +abraham hbc nehemiah nixon diligence" we now find that we get a total of 10 hits, 5 of which are relevant. This is a nice way to distill our search results into something more useful, but it is still underpowered in two senses. First, we had to do it by hand, thus violating the programmer's cardinal virtue of laziness[^16]. Second, we still haven't exploited the fact that we know something about the network that John Abraham was embedded in.  

What does that mean? Abraham's biography mentions John Marsh[^17], who was appointed governor of James Bay in 1688 and died that year or the following. And Marsh's biography mentions William Bond[^18] (fl 1655-94), captain of the Churchill. Now although Abraham's biography doesn't mention Bond at all, when we read Bond's biography we discover that he found the Mary in distress in Hudson Strait and took her company aboard, including John Abraham. Abraham's biography mentions that the Mary was wrecked by ice, but doesn't mention Bond. By following the links between various entites (people and ships in this case), we were able to discover new information. Techniques for link analysis automate this process of discovery.  

So what kind of database tables do we need? We want to keep each kind of entity in a separate table. We will have one table each for people, places, ships, documents, institutions, and so on. Each individual in one of these tables must be distinguished from all of the others, so we create what is called a primary key[^19] for each. Your name, which is not guaranteed to be unique, isn't a good primary key (think of "John Abraham"). Your social insurance number (or social security number) is supposed to be. We will just assign these primary keys automatically. Whenever we need information about one of our entities, we can look it up using the primary key.  

We will also want to create tables of links. These will contain a primary key (something to specify each unique link) and foreign keys[^19] for each entity that is linked. So, schematically, one entry in our link table might say "the person John Abraham is related to the ship Mary" (and specify how), and another might say that "the person William Bond is related to the institution HBC," and so on. We can then write programs to trace along these links trying to discover new information, or programs that can refine search results by drawing in related information.  

Tags: data mining[^20] \| dictionary of canadian biography[^21] \| link analysis[^22]  
 | new information[^23] | relational databases[^24] | search[^25] | social network analysis[^26]

---

Previous: [Brief Hiatus](20060301-brief-hiatus.md)  
Next: [Blogospheric Stock](20060310-blogospheric-stock.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2006/02/text-mining-dcb-part-5.html`
[^2]: `http://www.biographi.ca/EN`
[^3]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34253`
[^4]: `http://www.google.com/search?q=groseilliers`
[^5]: `http://www.collectionscanada.ca/explorers/h24-1460-e.html`
[^6]: `http://www.pbs.org/empireofthebay/profiles/rg.html`
[^7]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=35174`
[^8]: `http://www.google.com/search?q=radisson`
[^9]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34123`
[^10]: `http://www.siam.org/`
[^11]: `http://www.siam.org/meetings/archives.php#sdm`
[^12]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34171`
[^13]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34553`
[^14]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34703`
[^15]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34370`
[^16]: `http://blog.outer-court.com/archive/2005-08-24-n14.html`
[^17]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34520`
[^18]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34192`
[^19]: `http://www.utexas.edu/its/windows/database/datamodeling/dm/keys.html`
[^20]: `http://technorati.com/tag/data+mining`
[^21]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^22]: `http://technorati.com/tag/link+analysis`
[^23]: `http://technorati.com/tag/new+information`
[^24]: `http://technorati.com/tag/relational+databases`
[^25]: `http://technorati.com/tag/search`
[^26]: `http://technorati.com/tag/social+network+analysis`
