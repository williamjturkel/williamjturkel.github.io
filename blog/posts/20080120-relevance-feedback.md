# Relevance Feedback

_January 20, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/01/relevance-feedback.html`

Suppose Albert, Betty and Chris are historians of food, technology and Indonesia, respectively. It's not hard to imagine a scenario where each might sit down in front of Google and type "java" into the search box. One of the key problems of designing a search engine is trying to find a way to order the results so that the highest ranked hits will be relevant to the most users. In this case, let's assume that Google isn't tracking any of the three (i.e., they aren't logged in to GMail or other services and they aren't using their own computers). I just tried this search while logged in to Google and the top 12 results were relevant to the computer language, followed by one hit for the Indonesian island, followed by thirty-seven more for the computer language. I stopped counting. I love coffee, but I don't read about it or buy it online, so it is possible that my searching history helps Google know that I'm probably looking for information about the programming language. It's also possible that most people who use Google are looking for information about the programming language.  

Google's default assumption in this case is good news for Betty, and not such good news for Albert or Chris. Each of them could go on to refine their search, of course. One obvious possibility would be to add keywords ("java +coffee") or subtract them ("java -programming") or both. But the fact remains that Betty will find what she is looking for immediately, while the other two won't without more digging. It is easy to see how repeated experiences might shape a person's experience of the web, leading them to see it as a place of scarcity or abundance[^1].  

Without knowing more about what a particular searcher is after, it is very difficult to do better than to match the distribution of result relevance to something else that can be measured easily. That may be a measurement of the importance or centrality of sets of documents, or a survey of what users are looking for when they enter popular keywords, or any number of other measures singly or in or combination. Search engine companies can also measure the click-through for particular links. If most people click on one of the results on the first page of hits and then don't repeat or modify their search, the company can infer that the result was probably relevant to the searcher's needs.  

Machine learning methods are often categorized as "supervised" or "unsupervised." In the former case, the system gets feedback telling it what is, or even better, what is not, a correct answer. Unsupervised methods don't receive any feedback, which usually makes their task much more difficult. If we cast search engine relevance in these terms, we can see that the system faces a task which is only partially supervised at best.  

In informational retrieval systems that were created before the web, users typically learned to construct elaborate queries and to refine their queries based on the results that they received. These systems often included a way for the user to provide relevance feedback. In the context of the web, queries are typically only a word or two long, and most search engines don't include a mechanism for the searcher to provide direct relevance feedback. This may be good enough for web searchers taken as a group (it may even be optimal), but it imposes a cost on individual researchers. Researchers need to be able to find obscure sources, and the best way to do this is to pair them with a system that can learn from relevance feedback. Digital humanists need tools that go beyond the single box search[^2]. And we're probably going to have to write them ourselves.  

Tags: digital history[^3] \| machine learning[^4] \| search[^5]

---

Previous: [The Programming Historian](20080114-programming-historian.md)  
Next: [Freedom of Expression](20080204-freedom-of-expression.md)  
[Back to the blog archive](../README.md)

[^1]: `http://www.historycooperative.org/journals/ahr/108.3/rosenzweig.html`
[^2]: `http://www.dancohen.org/2006/04/17/the-single-box-humanities-search/`
[^3]: `http://technorati.com/tag/digital+history`
[^4]: `http://technorati.com/tag/machine+learning`
[^5]: `http://technorati.com/tag/search`
