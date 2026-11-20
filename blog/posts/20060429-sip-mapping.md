# SIP Mapping

_April 29, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/04/sip-mapping.html`

In an earlier post[^1], I mentioned the fact that Amazon[^2] keeps track of phrases that are distinctive to a small set of books. These SIPs (statistically improbable phrases) can be used to get some idea of the conceptual landscape in and around particular works, and thus can be used to generate bibliographies. Ideally, of course, the process could be automated. If machine-readable versions of the books were available, it could also be used as part of a text mining project.  

I haven't had a chance to do much programming recently so I thought I would put together a rudimentary hack[^3] to scrape SIPs and create a map. I also wanted to learn how to use the open source Graphviz[^4] visualization toolkit, so I used a Perl module[^5] to link to it. If you look at the code for the hack, you can see how simple it is to create pretty neat graphs. The figure below (1Mb) shows what happens when you start with Diamond's *Guns, Germs, and Steel* and follow the SIPs to adjacent books. The figure is more than 8,000 pixels wide, so you have to zoom in to see the detail ... and at that level it is pretty complicated. I will leave the implementation of a better graph browser for a future hack.  

![](https://web.archive.org/web/20060429im_/http://photos1.blogger.com/blogger/4745/1988/200/0393317552-thumb.png)  

Tags: digital history[^6] \| hacking[^7] \| open source[^8] \| perl[^9] \| SIPs[^10] \| text mining[^11] \| visualization[^12]

---

Previous: [My Folders at the McCord](20060425-my-folders-at-mccord.md)  
Next: [Developments at Kodak (and Elsewhere)](20060511-developments-at-kodak-and-elsewhere.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2005/12/teaching-young-historians-to-search.html`
[^2]: `http://www.amazon.com`
[^3]: `http://digitalhistory.uwo.ca/dhh/hacks/sip-map.pl.html`
[^4]: `http://www.graphviz.org/`
[^5]: `http://search.cpan.org/~lbrocard/GraphViz-2.02/lib/GraphViz.pm`
[^6]: `http://technorati.com/tag/digital+history`
[^7]: `http://technorati.com/tag/hacking`
[^8]: `http://technorati.com/tag/open+source`
[^9]: `http://technorati.com/tag/perl`
[^10]: `http://technorati.com/tag/sips`
[^11]: `http://technorati.com/tag/text+mining`
[^12]: `http://technorati.com/tag/visualization`
