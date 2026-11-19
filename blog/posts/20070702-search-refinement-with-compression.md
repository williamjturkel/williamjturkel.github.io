# Search Refinement with Compression

_July 2, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/07/search-refinement-with-compression.html`

A few days ago I described a way of using Cilibrasi and Vitányi's Normalized Compression Distance (NCD) to automatically cluster bibliographic entries[^1] from the online Dictionary of Canadian Biography. A compression algorithm keeps track of redundancies when it is compressing a string. If those redundancies also occur in another string, then the two strings have something in common (i.e., the redundancies). The NCD ranges from 0 (if the two strings are identical) to 1 (if there is absolutely no overlap). Details are in the original article and laid out in one of my earlier posts[^2].  

Compression can also be used to automatically refine searches. Suppose you are interested in the explorer Martin Frobisher. If you type "Frobisher" into Yahoo! some of the first few pages of hits are relevant and some are not. Usually you have to wade through the results (or specify more search keywords and hope you don't eliminate something interesting by being too specific.)  

An alternate strategy is to enter a broad search keyword (e.g., "Frobisher") and use the NCD to automatically compare the summary that Yahoo! returns for each hit with a "probe" text such as Frobisher's DCB entry. A short Python program to do exactly that is listed here[^3]. The search engine results can then be ranked according to increasing NCD from the probe text.  

The figure below shows the first 31 of 50 hits for "Frobisher" before and after this search refinement process. I used red font to indicate the irrelevant results. As can be seen, this use of compression and a probe text does a good job of floating the relevant hits to the top of the pile.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVHhJo_-1dAmitItBTtMiAmWHCcak5prD5FxP_tyqiutn4QnoSngeW-einUeWzOmr7tWhsyYMezhylPv6yOaHSzp2vRpTsJuA79xfeDJ9SbVItoVvwHQo33rWBQOjWLC0aSLJ59g/s200/frobisher-ncd-graph.png)  

Tags: data compression[^4] \| data mining[^5] \| Dictionary of Canadian Biography[^6] \| digital history[^7] \| Kolmogorov complexity[^8] \| search[^9] \| visualization[^10]

---

Previous: [Clustering with Compression](20070627-clustering-with-compression.md)  
Next: [History Appliances: Spöka](20070719-history-appliances-spka.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2007/06/clustering-with-compression.html`
[^2]: `http://digitalhistoryhacks.blogspot.com/2006/03/compression.html`
[^3]: `http://digitalhistory.uwo.ca/dhh/hacks/ncd-probe.py.html`
[^4]: `http://technorati.com/tag/data+compression`
[^5]: `http://technorati.com/tag/data+mining`
[^6]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^7]: `http://technorati.com/tag/digital+history`
[^8]: `http://technorati.com/tag/kolmogorov+complexity`
[^9]: `http://technorati.com/tag/search`
[^10]: `http://technorati.com/tag/visualization`
