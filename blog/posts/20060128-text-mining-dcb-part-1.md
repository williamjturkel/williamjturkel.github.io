# Text Mining the DCB, Part 1

_January 28, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/01/text-mining-dcb-part-1.html`

So far in our digital history hacks we have been working with the online Dictionary of Canadian Biography[^1]. The DCB has many properties which make it a good testbed for developing hacks. Unlike the American National Biography Online[^2] or the Oxford Dictionary of National Biography[^3], the DCB is freely available. With about 10,000 entries, it is also small enough to be easily processed, yet large enough to make computational methods worthwhile.  
  
Our previous hacks explored the categories to which the editors had already assigned many of the biographies. Our long-term goal, however, is to discover new information in online historical sources, both primary and secondary. Almost all of the existing works on digital history emphasize how new technologies and new media are changing the ways that we gather, preserve and present the past. (This is a paraphrase of the subtitle of Cohen & Rosenzweig's excellent Digital History[^4]; another example is David J. Staley's Computers, Visualization and History[^5].) This explosion of online sources also calls out for a new historical methodology, however. Over the next few decades, finding a 'methodology for the infinite archive' will require at least as significant a reorientation in historical practice as did the work of von Ranke[^6].  
  
The crux of the problem is simple: every year we are creating an untold amount of digital information. In 2003, researchers at the School of Information Management and Systems at UC Berkeley estimated that the amount of new information[^7] that had been created the previous year was about 37,000 times larger than the book collection of the Library of Congress[^8]. Ninety-two percent of that information was stored on magnetic media, mostly hard disks. Needless to say, this has serious implications for the practice of history (see, for example, David Talbot's article, "The Fading Memory of the State[^9].")  
  
Enter text mining[^10], an emerging field that draws on techniques from machine learning, computational linguistics, information retrieval and other disciplines to discover new information in unstructured data. (For a recent introduction to text mining, see Weiss et al, Text Mining[^11].)  
  
Using text mining on the DCB is going to be much more involved than anything we have done before, so we will proceed via a series of steps. The first thing that we want to do is create a local repository of the text to be mined. We go to the DCB website[^12], create a search page of biographies of interest, and save the HTML file. I will choose Volume 1 of the DCB, which has biographies of 592 individuals who died between AD 1000 and 1700, and save the file as "dcbo-vol1.html". Next, we write a short hack[^13] to scrape the IDs and names from that file, and save the new file as "dcbo-vol1-ids.txt[^14]". At this point we are almost ready to download the biographies.  
  
Before we do, however, we should first check the terms of use of the DCB site to make sure that we are not going to violate any of their policies[^15]. They say that the information can be reproduced for personal, noncommercial use "in part or in whole and by any means" without special permission. Good! We write another hack[^16] to download the 592 biographies from Volume 1 to our machine. (It is important when doing something like this to be a good citizen and not hammer their server, so be sure to code a small break between each download).  
  
Next, we will have to strip out all of the HTML formatting for each biography...  
  
(26 Sep 2008: Links to code updated)  
  
Tags: dictionary of canadian biography[^17] \| digital history[^18] \| hacking[^19] \| new information[^20] \| perl[^21] \| text mining[^22] \| web programming[^23]

[Back to the blog archive](../README.md)

[^1]: `http://www.biographi.ca/EN`
[^2]: `http://www.anb.org`
[^3]: `http://www.oxforddnb.com`
[^4]: `http://chnm.gmu.edu/digitalhistory/`
[^5]: `http://www.mesharpe.com/mall/resultsa.asp?Title=Computers,+Visualization,+and+History:+How+New+Technology+Will+Transform+Our+Understanding+of+the+Past+`
[^6]: `http://cliopolitical.blogspot.com/2005/08/introduction-to-historical_112482482753969170.html`
[^7]: `http://www.sims.berkeley.edu/research/projects/how-much-info-2003/index.htm`
[^8]: `http://www.loc.gov`
[^9]: `http://www.technologyreview.com/InfoTech/wtr_14583,258,p1.html`
[^10]: `http://www.sims.berkeley.edu/%7Ehearst/text-mining.html`
[^11]: `http://www.amazon.com/gp/product/0387954333/`
[^12]: `http://www.biographi.ca/EN/Search.asp`
[^13]: `http://digitalhistory.wikispot.org/DHH20060128-01`
[^14]: `http://digitalhistory.wikispot.org/DHH20060128-02`
[^15]: `http://www.biographi.ca/06_e.html`
[^16]: `http://digitalhistory.wikispot.org/DHH20060128-03`
[^17]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^18]: `http://technorati.com/tag/digital+history`
[^19]: `http://technorati.com/tag/hacking`
[^20]: `http://technorati.com/tag/new+information`
[^21]: `http://technorati.com/tag/perl`
[^22]: `http://technorati.com/tag/text+mining`
[^23]: `http://technorati.com/tag/web+programming`
