# Who is in the Dictionary of Canadian Biography?

_January 15, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/01/who-is-in-dictionary-of-canadian.html`

[A newer edition of this post is available here[^1]]  
  
When I was writing my dissertation in 2003, Libraries and Archives Canada put the Dictionary of Canadian Biography[^2] online, and made it freely available to scholars. Since I was in the US at the time, this made my life much easier. Instead of taking the subway to a library that had a copy of the DCB every time I needed to look someone up, I could now get biographical information without interrupting my writing.  
  
The online DCB has many other advantages over the print edition, however. For one thing, the entire text can be searched for keywords. If you are interested in a relatively obscure place that may no longer exist, you can immediately find the biographies that mention that place. If you search for "Fort Chilcotin," for example, you will only find one match, "Klatsassin[^3]." Most keywords that appear very infrequently will not make it into a printed index, making them almost impossible to find without full-text searching.  
  
Another advantage of online information is that it can often be made even more useful with a little bit of web programming. (For more on this idea see "Teaching Young Historians to Search, Spider and Scrape[^4].") Thus the first of our digital history hacks.  
  
On the advanced search page[^5] of the online DCB, it is possible to click on a volume number, geographical region, gender, or "identification" to see how many biographies match that category. Doing this shows that there are, for example, 450 biographies of females and 7,548 biographies of males. It is also possible to combine categories. There are 15 biographies of female aboriginal people and 229 biographies of male aboriginal people. Exploring the search page in such a desultory fashion can tell you a lot about Canadian historiography. Wouldn't it be nice to be able to automate this exploratory process?  
  
This hack scrapes the search page to extract the codes for each of the identification categories, then 'clicks' each category and grabs the number of matching biographies. The results are then presented as a "tag cloud," a representation where the font size is proportional to the number of hits. The code for the hack was written in Perl and is available here[^6]. The tag cloud of entries in the DCB looks like this:  
  
![](http://photos1.blogger.com/blogger/4745/1988/400/dcbo-cloud.jpg)  
  
Now what do we see? The vast majority of people in the DCB are businessmen, office holders, politicians, lawyers and soldiers. This, too, says a lot about Canadian historiography. It also suggests a new question: how do the categories change over time? That's another hack for another day.  
  
(26 Sep 2008: link to code was updated)  
  
Tags: dictionary of canadian biography[^7] | digital history[^8] | hacking[^9] | perl[^10] | tag cloud[^11]

[Back to the blog archive](../README.md)

[^1]: `http://williamjturkel.net/digital-history-hacks-2005-08/2006-01-15-who-is-in-the-dictionary-of-canadian-biography/`
[^2]: `http://www.biographi.ca`
[^3]: `http://www.biographi.ca/EN/ShowBio.asp?BioId=38649&query=`
[^4]: `http://digitalhistoryhacks.blogspot.com/2005/12/teaching-young-historians-to-search.html`
[^5]: `http://www.biographi.ca/EN/Search.asp`
[^6]: `http://digitalhistory.wikispot.org/DHH20060115-01`
[^7]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/hacking`
[^10]: `http://technorati.com/tag/perl`
[^11]: `http://technorati.com/tag/tag+cloud`
