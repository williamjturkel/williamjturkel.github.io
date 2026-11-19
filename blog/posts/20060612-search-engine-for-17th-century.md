# A Search Engine for 17th-Century Documents

_June 12, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/06/search-engine-for-17th-century.html`

One of the questions raised in the discussions today at the Doing Digital History workshop[^1] was how to make a search engine that returned documents written in a particular era. I'm assuming that we don't have access to metadata (that would be too easy). Here's the plan that I came up with. I haven't had a chance to try it yet, but it might make for some interesting hacking later on. Take the pages returned by a standard search engine, filter out any HTML or other markup tags and pass the plain text through a part-of-speech tagger[^2] to identify how each word is being used in context. After tagging, remove all of the stop words, things like 'and', 'the', 'is', etc. Now check each of the remaining words against an online etymological dictionary (like the Oxford English Dictionary[^3]) to determine the earliest attested date for each, and note whether the word has since fallen into disuse. You should end up with a vector of dates, the latest of which will put a bound on the earliest that the document could have been written. Less-common words will tend to be better indicators of date than more common ones, so it might help to take overall word frequency into account in the algorithm. The earliest date that this blog post could have been written, for example, would be bounded by the earliest attested dates of 'metadata' (1969), 'search engine' (1984), 'HTML' (1993) and 'blog post' (1999).  
  
Tags: dictionaries[^4] | Doing Digital History workshop[^5] | etymology[^6] | search[^7]

[Back to the blog archive](../README.md)

[^1]: `http://echo.gmu.edu/workshops/june2006/`
[^2]: `http://l2r.cs.uiuc.edu/~cogcomp/eoh/posdemo.html`
[^3]: `http://www.oed.com/`
[^4]: `http://technorati.com/tag/dictionaries`
[^5]: `http://technorati.com/tag/doing+digital+history+workshop`
[^6]: `http://technorati.com/tag/etymology`
[^7]: `http://technorati.com/tag/search`
