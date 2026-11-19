# Experimenting with the TAPoR Tools

_June 4, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/06/experimenting-with-tapor-tools.html`

This summer I'm in the process of developing a new graduate course on digital history. One of the things that we will study is the creation of online historical materials, and for this, I plan to assign Cohen and Rosenzweig's Digital History[^1]. I would also like to emphasize the new computational techniques that historians will increasingly need to use with digital sources. This raises some interesting challenges. I can't assume that my students will know how to program or that they will be familiar with markup languages like HTML or XML. We don't even really have time for the systematic exploration of a particular language, like Perl. (Although we will have time for some fun stuff[^2].) I've decided to focus on specific problems faced by historians working in the digital realm, and show how computation makes them tractable. I'll say more about the course in future posts; for now, suffice it to say that it will teach stepwise refinement[^3], be very hands-on and, no doubt, a bit hackish.  
  
The beta release of the TAPoR Text Analysis Portal[^4] gives students the chance to experiment with text processing without having to code everything from scratch. It allows the user to enter the URL of a digital source and then explore the text with an interactive concordance.  
  
For example, suppose you want to get (or convey) a sense of how the historian's job of interpretation can be augmented with computational tools. Go to the online Dictionary of Canadian Biography and choose an entry at random. I picked Robert McLaughlin[^5], someone with whom I wasn't already familiar. Using the TAPoR tool it is possible to find the most frequently occurring distinctive words and phrases in McLaughlin's biography:  
  

|  |
| --- |
| mclaughlin carriage |
| in oshawa |
| company |
| toronto |
| motor |
| automobiles |
| business |

  
It is also possible to get information about keywords in context. For example, clicking on "carriage" returns the following:  
  

|  |  |  |
| --- | --- | --- |
| Enniskillen, where he built a | carriage | works, which, in at least |
| him to build the Oshawa | Carriage | Works, a three-storey brick |
| which became known as McLaughlin | Carriage | about , was facilitated by careful |
| new designs (some influenced by | Carriage | Monthly, a Philadelphia journal), and |
| patents (and buying others), refining | carriage | mechanisms, tabulating the credit ratings |
| mostly wholesale business of McLaughlin | Carriage | is all the more impressive |
| transportation. Boosted as the largest | carriage | maker in the British empire |

  
Without reading the biography yet, I can now guess that Robert McLaughlin lived in Oshawa and founded a carriage works which became very successful. At this point, it is reasonable to object that I could have learned the same thing by reading his biography. The point, however, is that a computer can't learn by reading, but it can make use of text processing to produce more useful output. For example, suppose you wanted to create a "smarter" search engine. If you type "Robert McLaughlin" into Google, you get the following results.  
  

1. An art gallery in Oshawa
2. (ditto)
3. Bible Ministries
4. (ditto)
5. A photographer in Glasgow
6. An art gallery in Oshawa
7. A book about the battle of Okinawa in WWII
8. A role-playing game called "Cthulhu Live"
9. Realtors in New Jersey
10. The blog of a Californian graphic artist

  
 Now these results have less to do with one another than the animals in Borges' "Chinese Encyclopedia[^6]". But what if your search engine was to recognize "Robert McLaughlin" as a proper name, first submit the search to the Dictionary of Canadian Biography, process the text for keywords and then submit the query "Robert McLaughlin"+oshawa+carriage to Google? Then the first ten results would look like this:  
  

1. A Wikipedia entry on Oshawa with information about the McLaughlin Carriage Company
2. The Answers.com entry on Oshawa with information about the McLaughlin Carriage Company
3. A popular history website (Mysteries of Canada) with an article about the McLaughlin Carriage Company and General Motors
4. The history page of the City of Oshawa website with information about McLaughlin and his carriage company
5. An art gallery in Oshawa
6. The Canadian Encyclopedia entry on Oshawa with information about the McLaughlin Carriage Company
7. The Oshawa Community Museums and Archives page about the McLaughlin Carriage Company
8. An art gallery in Oshawa
9. An article about McLaughlin from the *Financial Post*, reproduced by the Business Library at the University of Western Ontario
10. A history page on the GM Canada website which talks about McLaughlin and his company

  
Tags: concordance[^7] | dictionary of canadian biography[^8] | digital history[^9] | history education[^10] | pedagogy[^11] | search[^12] | stepwise refinement[^13] | text mining[^14]

[Back to the blog archive](../README.md)

[^1]: `http://chnm.gmu.edu/digitalhistory/`
[^2]: `http://www.gtrlabs.com/node/90`
[^3]: `http://digitalhistoryhacks.blogspot.com/2006/05/blogging-andas-stepwise-refinement.html`
[^4]: `http://test-tapor.mcmaster.ca/portal/`
[^5]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=42074`
[^6]: `http://www.multicians.org/thvv/borges-animals.html?1`
[^7]: `http://technorati.com/tag/concordance`
[^8]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^9]: `http://technorati.com/tag/digital+history`
[^10]: `http://technorati.com/tag/history+education`
[^11]: `http://technorati.com/tag/pedagogy`
[^12]: `http://technorati.com/tag/search`
[^13]: `http://technorati.com/tag/stepwise+refinement`
[^14]: `http://technorati.com/tag/text+mining`
