# What We Need Now Is a Good Trolling Engine...

_September 9, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/09/what-we-need-now-is-good-trolling.html`

One thing that is difficult to do with a traditional search engine is find documents that were written at a particular time (the new Google News Archive Search[^1] being a notable exception). Suppose, for example, that you are starting a research project on the environmental history of nineteenth-century gold rushes in North America. Are there good collections of online primary sources that you should know about? Of course, but they can be hard to find. It would be great to be able to limit your Google searches to documents written during particular date ranges, e.g., 1848-55 (for the California[^2] gold rush), 1858-65 (Cariboo[^3]) or 1896-99 (Klondike[^4]).  
  
This turns out to be more difficult than you might think at first. Google Advanced Book Search[^5] allows you to specify a publication date range. So a search for "gold california date:1848-1855" returns books like Walter Colton's *Three Years in California[^6]* (1850), which you can actually download as a PDF. But other books are not going to show up, like *A Doctor's Gold Rush Journey to California[^7]* by Israel S. Lord, which was written from 1849 to 1851 but not published until 1995. In cases like these, you are searching through metadata rather than through the document itself. Most of the material on the web doesn't have enough metadata to be really satisfactory for this kind of searching.  
  
Furthermore, depending on the project you may not always have good search terms. Suppose you are thinking of becoming a digital medievalist[^8] and want to get some idea of what kinds of sources you might be able to work with. How do you search for machine-readable documents written in Old English? Obviously you will try to make use of the traditional scholarly apparatus and of online resource guides like The ORB[^9].  
  
To supplement this kind of activity, I'm thinking it would very nice to have what I'm going to call a "trolling engine," a tool that can sift through the Internet on a more-or-less continuous basis and return items that match a particular set of criteria determined by a human analyst. You would set it up, say, to look for documents written during the Cariboo gold rush, or written in Old English around the time of King Alfred, or those that may have be written by ornithologists in the West Midlands in the 1950s (if you're interested in the latter, you're in luck[^10]).  
  
So how would a trolling engine work? In present-day search engines, spiders scour the web downloading pages. A massive inverse index[^11] is created so that there is a link running from each term on every page back to the page itself. Once this blog post is indexed by Google's spiders, for example, there will be links to it in their inverse dictionary from "trolling," "engine," "spiders" and many other terms. The catch is that there is not a lot of other publicly-accessible information associated with each term. Suppose, however, that Google also tagged each term with its part-of-speech and parsed all the text in the surrounding context. Then you would be able to search for items in a particular syntactic frame. As Dan Brian showed in an interesting article[^12], you could search for all instances of "rock" used as an intransitive verb, and find sentences like "John thought San Francisco rocked" without finding ones like "The earthquake rocked San Francisco." There is already a pretty cool program called The Linguist's Search Engine[^13] that lets you do this kind of searching over a corpus of about 3.5 million sentences.  
  
In fact, being able to search the whole web for words in particular syntactic frames could be a very powerful historical tool for a simple reason: languages change over time. Take "sort of/kind of." For at least six hundred years, English speakers have been using these word sequences in phrases like "some kind of animal," that is, as a noun followed by a preposition. By the nineteenth century, "sort of" and "kind of" also appeared as degree modifiers: "I kind of think this is neat." In a 1994 Stanford dissertation, Whit Tabor[^14] showed that between the 16th and 19th centuries, "sort of" and "kind of" increasingly appeared in syntactic frames where either reading makes sense. That is, "kind of good idea" might be interpreted as [kind [of [good idea]]] or [[[kind of] good] idea]. So if you find a document that uses "sort of" or "kind of" as a degree modifier, you have one clue that it was probably written sometime after 1800. (See the discussion in Manning and Schütze[^15] for more on this example.)  
  
It's not just these two word sequences that have a history. Every word, every collocation[^16] has a history. A word like "troll" is attested as a verb in the fourteenth century and as a noun in the seventeenth. Its use as a fishing term also dates from the seventeenth century. If your document is about trolls it was probably written after 1600; if it is about trolling, it could have been written earlier (see my post on "A Search Engine for 17th-Century Documents[^17]"). By itself, the earliest attested date of a single word or collocation is weak evidence. If we were to systematically extract this kind of information from a very large corpus of dated documents, however, we could create a composite portrait of documents written in AD 890 or during the Cariboo gold rush or at any other given time.  
  
A similar logic would help us find documents written by ornithologists. In this case, the training corpus would have to be tagged with a different kind of metadata in addition to the date: the occupation of the author. Once we had that we could discover that two words that appear separately on millions of web pages, "pair" and "nested", occur quite rarely as the collocation "pair nested." That's the kind of thing an ornithologist would write.  
  
Tags: n-grams[^18] | perpetual analytics[^19] | search[^20] | spidering[^21] | text mining[^22] | trolling engine[^23]

[Back to the blog archive](../README.md)

[^1]: `http://news.google.com/archivesearch`
[^2]: `http://www.calisphere.universityofcalifornia.edu/calcultures/eras/era4.html`
[^3]: `http://collections.ic.gc.ca/cariboo/`
[^4]: `http://www.museum.nps.gov/klgo/page.htm`
[^5]: `http://books.google.com/advanced_book_search`
[^6]: `http://books.google.com/books?vid=0q-56wupvYSfsS&id=k-79tZ_KM6IC`
[^7]: `http://books.google.com/books?vid=ISBN0803279906`
[^8]: `http://www.digitalmedievalist.org/`
[^9]: `http://the-orb.net/`
[^10]: `http://www.westmidlandbirdclub.com/archive/reports1950s.htm`
[^11]: `http://www.google.com/librariancenter/articles/0512_01.html`
[^12]: `http://www.foo.be/docs/tpj/issues/vol5_3/tpj0503-0010.html`
[^13]: `http://lse.umiacs.umd.edu:8080/`
[^14]: `http://www.sp.uconn.edu/~ps300vc/tabor.html`
[^15]: `http://www.amazon.com/Foundations-Statistical-Natural-Language-Processing/dp/0262133601`
[^16]: `http://www.collins.co.uk/Corpus/CorpusSearch.aspx`
[^17]: `http://digitalhistoryhacks.blogspot.com/2006/06/search-engine-for-17th-century.html`
[^18]: `http://technorati.com/tag/ngrams`
[^19]: `http://technorati.com/tag/perpetual+analytics`
[^20]: `http://technorati.com/tag/search`
[^21]: `http://technorati.com/tag/spidering`
[^22]: `http://technorati.com/tag/text+mining`
[^23]: `http://technorati.com/tag/trolling+engine`
