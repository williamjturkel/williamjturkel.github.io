# Searching for History

_October 12, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/10/searching-for-history.html`

In August 2006, AOL released three months worth of search data for more than half a million of their users, each represented by a random ID number. Within days, the company realized that this was a mistake, withdrew the data and made a public apology. (If you missed the story you can find background information and news articles here[^1].) Many people created copies of the dataset before it was withdrawn and it is still available for download at various mirror sites on the web. Part of the uproar was due to the fact that people had used information like credit card and social security numbers in their searches; in one well-publicized case, a woman was actually identified by the content of her searches.  
  
The AOL researchers intended the data to be used for research purposes, and, in fact, it contains a wealth of information about everyday historical consciousness that is useful for public historians. With the proper tools, the AOL search data can be easily mined to discover what kinds of historical topics people are interested in and how they go about trying to find them. We can then use that information to shape the architecture[^2] of our online sites. The results presented below were generated in a couple of hours with off-the-shelf tools.  
  
The AOL data are distributed as a compressed archive which uncompresses to 10 text files totalling about 2.12 Gb. I used a program called TextPipe Pro[^3] to extract all of the searches with 'history' in them. I then loaded these into Concordance[^4], another commercial program, to do the text analysis. True to its name, Concordance lets you create concordances[^5] and tables of collocations[^6]. (Readers of this blog will know that both of these tasks could be easily accomplished with a programming language like Python[^7], but I wanted to show that you don't have to be able to program to do simple data mining.) The process of extracting the searches and creating a concordance for the 57291 tokens of 'history' was very fast. It took less than five minutes on a not-very-expensive desktop computer running Win XP.  
  
Given a concordance, we are in a position to explore what kinds of searches include the word 'history'. For example, suppose someone is interested in US History. They could frame their search in many ways: 'American history', 'history of the United States', and so on. If you are trying to reach users with an online history site, you want to know what kinds of searches they are going to use to get to you. The table below shows the various possibilities that were used by AOL searchers more than fifty times. (Note that I don't include searches for individual states, that the phrase 'American history' is a substring of other phrases like 'African American history' and 'Latin American history', and that the concordance program allows us to search for collocations separated by intervening words.)  
> american history 998  
> us history 379  
> american X history 99  
> history X american 92  
> united X history 85  
> states history 83  
> history X X america 78  
> us X history 67  
> american X X history 63  
> america history 62

  
  
These data seem to indicate a fairly strong preference for the adjectival form. People, in other words, prefer to think of the subject as American or US History rather than the History of the US or of America. The AOL data provide stronger evidence for this search than for most others, but the pattern appears in other regional or national contexts. For example, 'european history' (67) vs. 'history of europe' (3), 'chinese history' (32) vs. 'history of china' (17). More work would obviously be needed to make any kind of strong claim. And some thematic subjects show the opposite pattern, e.g., 'technology history' (4) vs. 'history of technology' (10).  
  
Digging in the search data reveals some unexpected patterns. Some people search for historical topics using a possessive like 'alaska's history' (11), 'canada's history' (5), or 'china's history' (2). When I was adding meta tags[^8] to our History Department website[^9], this one never occurred to me but it makes sense in retrospect. If you sort the data by the right context (the stuff that appears after the word 'history') you also find that many people are trying to use dates to limit their searches in a way that most search engines don't allow.  
> england history 1350 to 1850  
> french history 1400's  
> world history 1500 through 1850  
> world history 1500-1750  
> women history 1620-1776  
> italian history 1750's  
> ancient history 1735 bc  
> russian history 1880-1900  
> texas history 1890s law  
> texas history 1900s news  
> salvadoran history 1980s  
> east harlem history 19th century

  
  
Unfortunately, searching for '1400's' won't yield dates in the range 1400-1499, it will merely match the literal string '1400's'. Likewise, searching for '1350 to 1850' will only return pages that have '1350' or '1850' in them. Searching for '19th century' will give better results but still miss many relevant documents. I hope that companies that are working on search engines have noticed that people want to do these kind of searches, as it would make the web much more useful for historical research if you could.  
  
The prepositional form really comes into its own for more idiosyncratic searches. Apparently people want to know the histories of  
> 1892 carlsbad austria china[^10] teapots  
> a and w[^11] root beer  
> acne[^12]  
> alfredo sauce[^13]  
> banoffee pie[^14]  
> bingham hill cemetery[^15]  
> blood gangs and hand shakes[^16]  
> celtic body art[^17]  
> chakras[^18]  
> coleus plant[^19]  
> dental hygiene[^20] in america  
> do rags[^21]  
> easter egg[^22] hunt  
> emlen physick[^23]  
> everything video game[^24] releated  
> family feud[^25]  
> fat tuesday[^26]  
> girls sweet sixteen birthdays[^27]  
> gorzkie zale[^28]  
> half pipe[^29] in snowboarding  
> hex nuts[^30]  
> impala ss[^31]  
> irrational numbers[^32]  
> jang bo go[^33]  
> jay-z[^34]  
> k9 german sheppards[^35]  
> kissing[^36]  
> l'eggs[^37] hosiery  
> laminated dough[^38]  
> macho man[^39]  
> motion offense in basketball[^40]  
> myspace[^41]  
> nalgene[^42]  
> national pi day[^43]  
> oreos[^44]  
> paper marbling[^45]  
> patzcuaro[^46]  
> quad rugby[^47]  
> resident evil[^48]  
> residential wiring[^49] systems  
> salads[^50]  
> shaving legs[^51]  
> toilet paper[^52]  
> trolls[^53]  
> tv dinners[^54]  
> ultrasound[^55]  
> using wine[^56]  
> v8 juice[^57]  
> vikings ruins in okla[^58]  
> watts towers[^59]  
> wifebeaters[^60]  
> xbox[^61]  
> yankee doodle dandy[^62]  
> zombie movies[^63]

  
  
There's no adjectival form for these. The history of sport may be interesting to sport historians, but to whom is the history of hex nuts interesting? More people than you'd think.  
  
Finally, we can also see the AOL users' concern with privacy in the data. The concordance software allows us to see which words appear most frequently 1 position to the left of 'history' and 1 position to the right, 2 positions to the left and 2 positions to the right, and so on. The left collocations are most informative in this case. We find, for example, that 'clear' is the third most frequently appearing word 1 position to the left of 'history'. Fourteen hundred and thirteen different searches included the phrase 'clear history', 563 the phrase 'delete history' and 208 'erase history'. If we look 2 positions to the left, we find more searches with similar intent 'clear X history' (510), 'delete X history' (353) and 'erase X history' (140). Ironically, many of these searches also include 'AOL' as a collocate, e.g., 'how do i delete my history on aol' or 'remove my history from aol'. The table below summarizes these collocations.  
  

|  |  |  |  |
| --- | --- | --- | --- |
|  | my 199 | my 1836 | history |
| clear 123 | clear 510 | clear 1413 | history |
| aol 41 | aol 238 | aol 668 | history |
| delete 71 | delete 353 | delete 563 | history |
|  |  | search 382 | history |
|  | erase 140 | erase 208 | history |
|  |  | browser 132 | history |

  
Of course, this is merely the tip of the iceberg. Much more could be found by studying, for example, how people use dates in searches or what kinds of things they are looking for when they visit particular websites.  
  
Tags: AOL search data[^64] \| concordance[^65] \| data mining[^66] \| findability[^67] \| KWIC[^68] \| public history[^69] \| search[^70] \| text mining[^71]

[Back to the blog archive](../README.md)

[^1]: `http://digitalhistory.uwo.ca/quarry/aol-search-story.php`
[^2]: `http://www.amazon.com/Information-Architecture-World-Wide-Web/dp/0596527349/`
[^3]: `http://www.crystalsoftware.com.au/textpipe.html`
[^4]: `http://www.concordancesoftware.co.uk/`
[^5]: `http://www.cch.kcl.ac.uk/legacy/teaching/av1000/textanalysis/concord.html`
[^6]: `http://www.cch.kcl.ac.uk/legacy/teaching/av1000/textanalysis/method.html`
[^7]: `http://www.python.org`
[^8]: `http://searchenginewatch.com/showPage.html?page=2167931`
[^9]: `http://history.uwo.ca/`
[^10]: `http://en.wikipedia.org/wiki/Porcelain`
[^11]: `http://www.awrestaurants.com/`
[^12]: `http://en.wikipedia.org/wiki/Acne`
[^13]: `http://en.wikipedia.org/wiki/Alfredo_%28sauce%29`
[^14]: `http://en.wikipedia.org/wiki/Banoffee_Pie`
[^15]: `http://www.worldcat.org/oclc/40726372&referer=brief_results`
[^16]: `http://en.wikipedia.org/wiki/Gang_signal`
[^17]: `http://en.wikipedia.org/wiki/History_of_tattooing`
[^18]: `http://en.wikipedia.org/wiki/Chakras`
[^19]: `http://en.wikipedia.org/wiki/Coleus`
[^20]: `http://en.wikipedia.org/wiki/Dental_hygiene`
[^21]: `http://en.wikipedia.org/wiki/Do_rag`
[^22]: `http://en.wikipedia.org/wiki/Easter_egg`
[^23]: `http://www.welshcolor.com/physick.html`
[^24]: `http://en.wikipedia.org/wiki/Video_games`
[^25]: `http://en.wikipedia.org/wiki/Family_feud`
[^26]: `http://en.wikipedia.org/wiki/Fat_Tuesday`
[^27]: `http://en.wikipedia.org/wiki/Sweet_sixteen_%28birthday%29`
[^28]: `http://acweb.colum.edu/users/agunkel/homepage/easter/eastgz.html`
[^29]: `http://en.wikipedia.org/wiki/Half_pipe`
[^30]: `http://www.boltdepot.com/nuts.aspx`
[^31]: `http://en.wikipedia.org/wiki/Chevrolet_Impala_SS`
[^32]: `http://mathworld.wolfram.com/IrrationalNumber.html`
[^33]: `http://en.wikipedia.org/wiki/Jang_Bo-go`
[^34]: `http://en.wikipedia.org/wiki/Jay-z`
[^35]: `http://en.wikipedia.org/wiki/German_shepard`
[^36]: `http://en.wikipedia.org/wiki/Kissing`
[^37]: `http://www.leggs.com/`
[^38]: `http://www.freepatentsonline.com/5182123.html`
[^39]: `http://en.wikipedia.org/wiki/Macho_man`
[^40]: `http://en.wikipedia.org/wiki/Motion_offense`
[^41]: `http://www.myspace.com`
[^42]: `http://en.wikipedia.org/wiki/Nalgene`
[^43]: `http://www.exploratorium.edu/pi/index.html`
[^44]: `http://en.wikipedia.org/wiki/Oreo`
[^45]: `http://en.wikipedia.org/wiki/Paper_marbling`
[^46]: `http://en.wikipedia.org/wiki/Patzcuaro`
[^47]: `http://en.wikipedia.org/wiki/Quad_Rugby`
[^48]: `http://en.wikipedia.org/wiki/Resident_Evil`
[^49]: `http://en.wikipedia.org/wiki/Electrical_wiring_%28United_States%29`
[^50]: `http://en.wikipedia.org/wiki/Salads`
[^51]: `http://en.wikipedia.org/wiki/Leg_shaving`
[^52]: `http://en.wikipedia.org/wiki/Toilet_paper`
[^53]: `http://en.wikipedia.org/wiki/Trolls`
[^54]: `http://en.wikipedia.org/wiki/TV_Dinner`
[^55]: `http://en.wikipedia.org/wiki/Ultrasound`
[^56]: `http://en.wikipedia.org/wiki/Wine`
[^57]: `http://en.wikipedia.org/wiki/V8_juice`
[^58]: `http://www-csli.stanford.edu/~nunberg/infolit.html`
[^59]: `http://en.wikipedia.org/wiki/Watts_towers`
[^60]: `http://en.wikipedia.org/wiki/Wifebeater_%28slang%29`
[^61]: `http://en.wikipedia.org/wiki/Xbox`
[^62]: `http://en.wikipedia.org/wiki/Yankee_doodle`
[^63]: `http://www.imdb.com/find?q=zombies`
[^64]: `http://technorati.com/tag/aol+search+data`
[^65]: `http://technorati.com/tag/concordance`
[^66]: `http://technorati.com/tag/data+mining`
[^67]: `http://technorati.com/tag/findability`
[^68]: `http://technorati.com/tag/kwic`
[^69]: `http://technorati.com/tag/public+history`
[^70]: `http://technorati.com/tag/search`
[^71]: `http://technorati.com/tag/text+mining`
