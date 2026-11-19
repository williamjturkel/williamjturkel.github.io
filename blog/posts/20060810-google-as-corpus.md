# Google as Corpus

_August 10, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/google-as-corpus.html`

Last year, the Economist noted that corpus linguists[^1] are increasingly turning to the world wide web as a model of what people actually say ("Corpus colossal[^2]," 20 Jan 2005). There are complications, to be sure, many of them caused by the never-ending war on spam[^3]. To a good first approximation, however, it is possible to mine the web for examples of common and not-so-common phrasing. Many of these techniques have applications for digital history.  
  
Consider the problem of trying to find a good keyword when searching through sources, or for indexing a compilation of documents. How can we program a computer to figure out what a document is about? We might start with a measure of how frequently particular words occur. (For this we can use one of the TaPOR tools[^4]). Suppose we find that document D contains multiple copies of words like 'state' (24 times), 'water' (23), 'Chinese' (17), 'San Francisco' (10), 'steamer' (6) and 'telegraph' (3). The document could be about anything, but a historian might reasonably guess that it was about California in the 19th century.  
  
Frequency is not enough by itself. Document D also contains multiple copies of 'the' (313), 'of' (145), 'and' (144), 'in' (89) and many other words that do little to distinguish it from other documents written in English. As a result, specialists in information retrieval[^5] have created a measure called tf-idf[^6], which weights the frequency of a given term by its relative infrequency in the corpus as a whole. Here's where Google comes in. When you search for a term, the search engine responds with the number of pages that contain that term. A couple of years ago, Philipp Lenssen used the Google API to determine the frequency of the 27,693 most used words[^7]. At the time, the word 'the' appeared in 522 million pages. The web has grown since then: three years later 'the' appears in about 42 times as many pages.  
  
If we look for words in document D that have a relatively high tf-idf (using Google as our corpus), we can come up with a set of potential keywords, shown in the table below. Note that even the least frequent of these occurs in more than half a million documents on the web.  
  

|  |  |
| --- | --- |
| chinese | 859,000,000 |
| mud | 66,900,000 |
| steamer | 9,680,000 |
| Tuolumne | 2,070,000 |
| Alviso | 931,000 |
| Ashburner | 635,000 |

  
  
When we use the keywords together, however, we can pick our document D out of the billions that Google indexes. The table below shows the number of hits for each, more narrow search.  
  

|  |  |
| --- | --- |
| chinese | 859,000,000 |
| chinese mud | 5,830,000 |
| chinese mud steamer | 141,000 |
| chinese mud steamer Tuolumne | 621 |
| chinese mud steamer Tuolumne Alviso | 70 |
| chinese mud steamer Tuolumne Alviso Ashburner | 1 |

  
  
Used in conjunction with the Google Search API, in other words, a metric like tf-idf can automatically find the set of keywords which will return a given document. We can then find similar documents by relaxing the search a little bit and seeing what else turns up.  
  
Besides frequency, we can also consider the context that a given keyword appears in. One way to do this is by simply searching for seemingly characteristic phrases. "Blunts the keener feelings," for example, is apparently unique to document D, as is "muddy, cheerless and dull beyond telling." There are some specialized tools, like the Linguist's Search Engine[^8], which allow the user to search for grammatical structures. You can tell it that you want to find constructions like "the bigger the house the richer the buyer" and it will return with things like "the darker the coffee bean, then the less caffeine." (See the 2005 paper[^9] by Resnik, Elkiss, Lau and Taylor for more info.)  
  
Until now Google has kept most of the raw data to themselves, generously providing an API for researchers to access some of it. On August 3rd, however, they announced[^10] that they would be making more than a billion 5-grams available to researchers. An n-gram is a sequence of tokens, words in this case, that you get by sliding a window across text. If S is the previous sentence, then you can generate all of the 5-grams with a one-line Python[^11] script  
 `print [S[i:i+5] for i in range(len(S)-4)]`  
which returns  
> [['an', 'n-gram', 'is', 'a', 'sequence'],  
> ['n-gram', 'is', 'a', 'sequence', 'of'],  
> ['is', 'a', 'sequence', 'of', 'tokens'],  
> ['a', 'sequence', 'of', 'tokens', 'words'],  
> ['sequence', 'of', 'tokens', 'words', 'in'],  
> ['of', 'tokens', 'words', 'in', 'this'],  
> ['tokens', 'words', 'in', 'this', 'case'],  
> ['words', 'in', 'this', 'case', 'that'],  
> ['in', 'this', 'case', 'that', 'you'],  
> ['this', 'case', 'that', 'you', 'get'],  
> ['case', 'that', 'you', 'get', 'by'],  
> ['that', 'you', 'get', 'by', 'sliding'],  
> ['you', 'get', 'by', 'sliding', 'a'],  
> ['get', 'by', 'sliding', 'a', 'window'],  
> ['by', 'sliding', 'a', 'window', 'across'],  
> ['sliding', 'a', 'window', 'across', 'text']]

  
  
The Google research team did something similar on more than a trillion words from the web, and kept every 5-gram that occurred more than forty times. (Which means that "cheerless and dull beyond telling" won't be in the data set, since it occurs only once, in document D.)  
  
So what can you do with n-grams? Lots. Daniel Tauritz, a computer scientist at the University of Missouri-Rolla keeps a clearinghouse[^12] of n-gram research. A partial list of applications includes "text compression (1953), spelling error detection and correction (1962), optical character recognition (1967), information retrieval (1973), textual representation (1979), language identification (1991), missing phoneme guessing (1992), information filtering (1993), automatic text categorization (1994), music representation (1998), spoken document retrieval (2000), computational immunology (2000) and medical record matching (2001)." Many of these techniques have clear applications or analogs in historical research.  
  
Tags: application program interface[^13] \| Google[^14] \| n-grams[^15] \| python[^16] \| search[^17] \| statistical natural language processing[^18] \| tf-idf[^19]

[Back to the blog archive](../README.md)

[^1]: `http://en.wikipedia.org/wiki/Corpus_linguistics`
[^2]: `http://www.economist.com/science/displayStory.cfm?story_id=3576374`
[^3]: `http://en.wikipedia.org/wiki/Email_spam`
[^4]: `http://test-tapor.mcmaster.ca/portal/portal`
[^5]: `http://en.wikipedia.org/wiki/Information_retrieval`
[^6]: `http://en.wikipedia.org/wiki/Tf-idf`
[^7]: `http://blog.outer-court.com/archive/2003_11_03_index.html`
[^8]: `http://lse.umiacs.umd.edu:8080/`
[^9]: `http://www-personal.umich.edu/~aelkiss/papers/lse_bls2005.pdf`
[^10]: `http://googleresearch.blogspot.com/2006/08/all-our-n-gram-are-belong-to-you.html`
[^11]: `http://www.python.org/`
[^12]: `http://web.umr.edu/~tauritzd/ngram/`
[^13]: `http://technorati.com/tag/application+program+interface`
[^14]: `http://technorati.com/tag/Google`
[^15]: `http://technorati.com/tag/ngrams`
[^16]: `http://technorati.com/tag/python`
[^17]: `http://technorati.com/tag/search`
[^18]: `http://technorati.com/tag/statistical+natural+language+processing`
[^19]: `http://technorati.com/tag/tfidf`
