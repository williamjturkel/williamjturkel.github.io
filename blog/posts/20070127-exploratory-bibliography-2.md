# Exploratory Bibliography 2: Visualization

_January 27, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/01/exploratory-bibliography-2.html`

A few days ago I posted a hack[^1] that scraped my digital history reading list[^2] and submitted each book in turn to the Amazon API to get further recommendations. We saved a large list of book pairs ("if you liked that you'll also like this") for further hacking. Given such a list, it is quite easy to convert it to a script that can be fed into the freely available Graphviz[^3] program, which allows us to visualize the connections between books as a network of recommendations. The Python code for doing that is here[^4]; the graph subsequently output by Graphviz is below. (Since the image is pretty big, it is easier to work with if you download it to your own machine and use a graphics program to zoom in and out.)  

![](../images/20070127-exploratory-bibliography-2-1.jpg)  

The whole point about visualization, of course, is that it should enable us to see things we might otherwise have missed. When we look at the network of recommendations that connects books on the reading list, we notice a number of interesting patterns.  

![](../images/20070127-exploratory-bibliography-2-2.jpg)  

**Monads and dyads**. There are a number of books that aren't related by recommendation to any of the others on the list. The one shown in the figure here is Sconce's *Haunted Media*. Recommended items in the Amazon catalog include other books about haunting and more general books about popular media. There are also a number of pairs where one or both of the books recommends the other. The examples shown here are Clark's *Natural Born Cyborgs* -> Clark's *Being There*, Staley's *Computers, Visualization, and History* -> Cohen and Rosenzweig's *Digital History*, and Garfinkel's *Database Nation* &lt;-> O'Harrow's *No Place to Hide*.  

![](../images/20070127-exploratory-bibliography-2-3.jpg)  

**A classic cluster**. This tightly knit cluster consists of four books that have attained 'classic' status in new media and digital humanities: Laurel's *Computers as Theater* (1991), Aarseth's *Cybertext* (translated 1997), Murray's *Hamlet on the Holodeck* (1998), and Manovich's *Language of New Media* (2002). The fact that none of these well-known works is a recommended accompaniment to anything on the list that was published more recently suggests that it might be worth searching more generally for temporal strata in networks of recommendations.  

![](../images/20070127-exploratory-bibliography-2-4.jpg)  

![](../images/20070127-exploratory-bibliography-2-5.jpg)  

**The bridge and the subcluster**. One of the more interesting things about this network is that there is a single book linking the main body of the network with a fairly large and tightly knit subcluster. The bridging book is Langville and Meyer's introduction to search engine ranking *Google's PageRank and Beyond*. The books at the center of the subcluster include Baeza-Yates and Ribeiro-Neto's *Modern Information Retrieval*, Manning and Schütze's *Foundations of Statistical NLP*, Grossman and Frieder's *Information Retrieval*, Weiss et al's *Text Mining*, Belew's *Finding Out About*, Witten, Moffat and Bell's *Managing Gigabytes*, Chakrabarti's *Mining the Web*, and Witten and Frank's *Data Mining*. These books form the technical core of the reading list. The fact that they're outside the network of recommendations for more general readings on digital humanities highlights the divide that I'm trying to bridge with this blog.  

![](../images/20070127-exploratory-bibliography-2-6.jpg)  

**Bestsellers**. A few of the books in the network are distinguished by a large number of incoming recommendations. The three shown here are Morville's *Ambient Findability* (Amazon sales rank 2,797), Jenkins's *Convergence Culture* (3,347), and Benkler's *Wealth of Networks* (6,745). Besides serving as 'hubs' in a recommendation network, it is also useful to keep these books in mind when communicating with people outside the discipline, for they are most likely to serve as common ground. (I often have conversations where someone asks me what environmental history is, I start to tell them, then they say, "Oh, you mean like *Guns, Germs and Steel*." Amazon sales rank? 199.)  

One of the objectives of a comprehensive / general exam is to learn how to do things with a stack of books: to trace the origins of ideas or concepts, find pairings or clusters that would work well together in a syllabus, find key works that are emblematic of a particular school, and so on. Digital approaches like the one demonstrated here can be very useful in this process.  

Tags: Amazon[^5] \| application program interface[^6] \| bibliography[^7] \| Graphviz[^8] \| hacking[^9] \| python[^10] \| visualization[^11]

---

Previous: [Exploratory Bibliography](20070125-exploratory-bibliography.md)  
Next: [Keywords and Clues](20070130-keywords-and-clues.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2007/01/exploratory-bibliography.html`
[^2]: `http://digitalhistoryhacks.blogspot.com/2007/01/readings-for-field-in-digital-history.html`
[^3]: `http://www.graphviz.org/`
[^4]: `http://digitalhistory.uwo.ca/dhh/hacks/exploratory-bibliography-03.py.html`
[^5]: `http://technorati.com/tag/amazon`
[^6]: `http://technorati.com/tag/application+program+interface`
[^7]: `http://technorati.com/tag/bibliography`
[^8]: `http://technorati.com/tag/graphviz`
[^9]: `http://technorati.com/tag/hacking`
[^10]: `http://technorati.com/tag/python`
[^11]: `http://technorati.com/tag/visualization`
