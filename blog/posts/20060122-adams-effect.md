# The Adams Effect

_January 22, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/01/adams-effect.html`

[A newer edition of this post is available here[^1]]  
  
In an earlier hack[^2] we discovered that the majority of people in the *Dictionary of Canadian Biography*[^3] were categorized as businessmen, office holders, politicians, lawyers and soldiers. The biographies cover a 930-year span, however, which raises the question of which occupations were prevalent at any particular time. One might suspect, for example, that there were relatively fewer explorers and fur traders in more recent years. We can call this the "Adams Effect," after a passage from a letter that John Adams wrote to Abigail Adams in 1780. (Not to be confused with Pepper Adams's final album[^4] of the same name.) Anyway, John Adams said  
> I must study politics and war that my sons may have liberty to study mathematics and philosophy, geography, natural history, naval architecture, navigation, commerce, and agriculture, in order to give their children a right to study painting, poetry, music, architecture, statuary, tapestry, and porcelain.

  
  
Does this capture the Canadian experience? Time for another hack[^5]. To save time, we scrape the search page and extract the codes for the different volumes and categories. Biographies in four of the twelve volumes haven't been categorized, so there will be some gaps in our data, but we should have enough to see trends. We build a table of data[^6] to analyze in a spreadsheet. We can then plot the relative proportion of each occupation over time. (Relative because there are more biographies overall in some volumes.) Also, since some occupations are very common (e.g., member of armed forces) and others are not (e.g., architect) we will want to plot the numbers on a log scale[^7]. The following three graphs show which occupations lose, maintain or gain ground over time.  
  
![](http://photos1.blogger.com/blogger/4745/1988/200/ids-chg-down.jpg)  
  
![](http://photos1.blogger.com/blogger/4745/1988/200/ids-chg-even.jpg)  
  
![](http://photos1.blogger.com/blogger/4745/1988/200/ids-chg-up.jpg)  
  
So, is there an "Adams Effect" in Canadian biography? His "war" prediction is spot on: almost 21% of the biographies in Volumes 2 (1701-40) and 4 (1771-1800) are for members of the armed forces. This drops steadily to about 4 or 5% by the late nineteenth century. "Politics," alas, becomes more, rather than less, popular, accounting for about 10% of the biographies in the first half of the nineteenth century, and peaking at about 14% in Volume 11 (1881-90). It is worth emphasizing the fact that the volumes of the *DCB* are organized by death dates, and that politicians who died in the 1880s may well have been active in the 1860s and 70s (i.e., during the Canadian Confederation[^8] and its aftermath.)  
  
How about the next generation? We see a decline in explorers and mariners, in the fur trade and agriculture. Surveying and engineering hold relatively steady. In the final generation we do see an increase in architects, authors and educators. Some predictions (like "statuary," "tapestry" and "porcelain") are harder to check. Overall, not too bad for a statement which was never intended as a prediction.  
  
(26 Sep 2008: links to code updated)  
  
Tags: dictionary of canadian biography[^9] \| digital history[^10] \| hacking[^11] \| perl[^12]

[Back to the blog archive](../README.md)

[^1]: `http://williamjturkel.net/digital-history-hacks-2005-08/2006-01-22-the-adams-effect/`
[^2]: `http://digitalhistoryhacks.blogspot.com/2006/01/who-is-in-dictionary-of-canadian.html`
[^3]: `http://www.biographi.ca/EN`
[^4]: `http://www.allmusic.com/cg/amg.dll?p=amg&sql=10:2fzsa9qgy23d%7ET00`
[^5]: `http://digitalhistory.wikispot.org/DHH20060122-01`
[^6]: `http://digitalhistory.wikispot.org/DHH20060122-02`
[^7]: `http://en.wikipedia.org/wiki/Log_scale`
[^8]: `http://www.collectionscanada.ca/confederation/index-e.html`
[^9]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^10]: `http://technorati.com/tag/digital+history`
[^11]: `http://technorati.com/tag/hacking`
[^12]: `http://technorati.com/tag/perl`
