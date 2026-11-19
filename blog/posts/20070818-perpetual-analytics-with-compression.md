# Perpetual Analytics with Compression

_August 18, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/08/perpetual-analytics-with-compression.html`

Perpetual analytics is the process of comparing each new item of incoming information to the whole collection at the moment that it is received. IBM scientist Jeff Jonas writes[^1], "there is an ocean of historical data and it is raining, which is to say new data keeps being introduced ... Think of [perpetual analytics] like 'directing the rain drops' as they fall into the ocean – placing each drop in the right place and measuring the ripples (i.e., finding relationships and relevance to the historical knowledge). Discovery is made during ingestion and relevant insight is published at that magical moment." Jonas contrasts this approach with the more traditional process of creating isolated, specialized databases to hold different kinds of information. Over time, these databases tend to become 'silos': many interesting things might be discovered if the information within them could be integrated, but the information costs[^2] are too high to do so.  
  
The most powerful implementation of this idea (not to mention the most difficult) would be general-purpose mining at the scale of the internet. I'll leave that for Google or IBM. Instead, I'm going to describe a special-purpose system that operates in a very restricted and small domain.  
  
Imagine browsing through a collection of online primary sources that may be relevant for your research. They could be diary entries, historic newspaper articles or parliamentary records. As you navigate to each new page, a set of links appears in the right sidebar, the way that sponsored advertisements appear in Google search results. Instead of being ads, however, these are links to related primary and secondary sources. If you are reading a letter, for example, there may be links in the sidebar to biographies of the author, recipient or people mentioned in the text. There may be links to other letters written by these people, or to other letters written at the same time and place. If some known event is being described, there may be links to historical accounts of that event. And so on. If you click on one of these sidebar links, a new tab opens in your browser with that source displayed in it, and with links to other sources that are related to it. The sidebar provides ambient information that may be useful without distracting you from the task at hand.  
  
This recommendation system has two very useful features: it is generated automatically and it gets smarter as you use it. Here's what is going on behind the scenes. When you browse to a page, the system stores a copy of the text in a database. If it is the first page you've ever looked at, nothing else happens. When you go to the second page, however, it stores a copy of the text, then uses the normalized compression distance (NCD) to determine how similar the two pages are. (For more on the NCD, see my earlier posts[^3].) As you browse to each new page, a copy is added to the database, and the NCD is calculated for that page and every other that one you've already visited. The sidebar displays links to the closest ones already in the database.  
  
As described so far, this system is able to cluster your own reading, always showing you links to the most relevant stuff that you've already seen. In order to be really useful, you can seed the database with source collections that are likely to be relevant but are too large to be read systematically. For example, if you are working in a particular national and temporal context, you might add all of the entries from a dictionary of historical biography. If you are working in a particular place, you might add complete runs of local newspapers. For specific fields you could add runs of scholarly journals. For groups of people you could add correspondence and diaries.  
  
Furthermore, the system scales up powerfully for collaborative research if the database is shared by everyone working on a particular subject. As each person finds something of interest, it immediately becomes available for recommendation to any of the others, depending on what they are looking at. Built on top of a server-backed version of Zotero[^4], this tool provides one path to leveraging the power of collective intelligences[^5].  
  
Tags: ambience[^6] \| browser[^7] \| data compression[^8] \| data mining[^9] \| Kolmogorov complexity[^10] \| perpetual analytics[^11] \| Zotero[^12]

[Back to the blog archive](../README.md)

[^1]: `http://jeffjonas.typepad.com/jeff_jonas/2006/02/what_do_you_kno.html`
[^2]: `http://digitalhistoryhacks.blogspot.com/2006/04/information-costs.html`
[^3]: `http://digitalhistoryhacks.blogspot.com/search?q=ncd`
[^4]: `http://www.zotero.org/`
[^5]: `http://digitalhistoryhacks.blogspot.com/2006/12/pedagogy-for-collective-intelligence.html`
[^6]: `http://technorati.com/tag/ambience`
[^7]: `http://technorati.com/tag/browser`
[^8]: `http://technorati.com/tag/data+compression`
[^9]: `http://technorati.com/tag/data+mining`
[^10]: `http://technorati.com/tag/kolmogorov+complexity`
[^11]: `http://technorati.com/tag/perpetual+analytics`
[^12]: `http://technorati.com/tag/zotero`
