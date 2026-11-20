# Exploratory Bibliography

_January 25, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/01/exploratory-bibliography.html`

A couple of weeks ago, I posted a reading list[^1] for a graduate exam in digital history. These kinds of lists are customarily around 80-100 books, so I didn't have room to include everything that's in my digital history library, or even everything that seemed essential (the list is quite light on programming books, for example.) Some of my students and colleagues were kind enough to send me suggested additions, which I may include in a subsequent post.  

It's been quite a while since I posted a hack, so I decided to do something with the reading list. Suppose you're interested in digital history and you want to know what other books I might've included on the list, or what similar books someone else might have recommended. Is there any way to automate the process of searching for similar books? Sure.  

The first step is to get a complete set of recommendations via the Amazon API. We pass my blog post through a simple scraper[^2] to get the ASINs (Amazon Standard ID Numbers) for each book on the list. In a loop, we then submit each ASIN to Amazon and get back an XML file that includes ASINs for recommended books. We create a big list of (ASIN, ASIN) pairs. Each one of these is a recommendation: customers who bought the first book also bought the second one. Since we will want to play with these data later on, we use a high-level Python module called pickle[^3] to save them to disk. Python source code for the first step is here[^4].  

Now that we've got a big list of recommendations, the second step is to concentrate on the books that come up most frequently. We unpickle our data then create a list of recommended books and filter out[^5] any that appear on the original list. We count the number of times each is recommended and sort to create a frequency list[^6] with most frequently recommended books at the top of the list. Python source for the second step is here[^7].  

(In the two steps above, I've linked to earlier posts on doing simple tasks with Python. If you compare those posts with the source code presented here, you can see how I modified code that I had already written to solve new problems.)  

So how well did it do? All of the books that were recommended four or more times appear in the list below. I have most of them and think any could easily have been included on the original list.  

* Anderson, Chris. The Long Tail: Why the Future of Business is Selling Less of More[^8]. Hyperion, 2006. [10 recommendations]
* Baker, Nicholson. Double Fold: Libraries and the Assault on Paper[^9]. Vintage, 2002. [4]
* Berry, Michael, ed. Survey of Text Mining: Clustering, Classification and Retrieval[^10]. Springer, 2003. [6]
* Berry, Michael and Murray Browne. Understanding Search Engines: Mathematical Modeling and Text Retrieval[^11]. SIAM, 2005. [6]
* Campbell-Kelly, Martin and William Aspray. Computer: A History of the Information Machine[^12], 2nd ed. Westview, 2004. [4]
* Greenfield, Adam. Everywhere: The Dawning Age of Ubiquitous Computing[^13]. Peachpit, 2006. [10]
* Hiltzik, Michael A. Dealers of Lightning: Xerox PARC and the Dawn of the Computer Age[^14]. Collins, 2000. [4]
* Hutchins, Edwin. Cognition in the Wild[^15]. MIT, 1996. [4]
* Jackson, Peter and Isabelle Moulinier. Natural Language Processing for Online Applications: Text Retrieval, Extraction, and Categorization[^16]. John Benjamins, 2002. [4]
* Jenkins, Henry. Fans, Bloggers, and Gamers: Media Consumers in a Digital Age[^17]. NYU, 2006. [4]
* Kuhn, Thomas S. The Structure of Scientific Revolutions[^18], 3rd ed. Chicago, 1996. [4]
* Lanham, Richard A. The Electronic Word: Democracy, Technology, and the Arts[^19]. Chicago, 1995. [5]
* Litman, Jessica. Digital Copyright: Protecting Intellectual Property on the Internet[^20]. Prometheus, 2000. [5]
* Moggridge, Bill. Designing Interactions[^21]. MIT, 2006. [4]
* Ryan, Marie-Laure. Narrative as Virtual Reality: Immersion and Interactivity in Literature and Electronic Media[^22], new ed. Johns Hopkins, 2003. [4]
* Standage, Tom. The Victorian Internet[^23]. Berkeley, 1999. [6]
* Suchman, Lucy A. Plans and Situated Actions: The Problem of Human-Machine Communication[^24]. Cambridge, 1987. [4]
* Sunstein, Cass R. Infotopia: How Many Minds Produce Knowledge[^25]. Oxford, 2006. [4]
* Vaidhyanathan, Siva. The Anarchist in the Library: How the Clash between Freedom and Control is Hacking the Real World and Crashing the System[^26], new ed. Basic, 2005. [4]
* Waldrop, M. Mitchell. The Dream Machine: J.C.R. Licklider and the Revolution that Made Computing Personal[^27]. Penguin, 2002. [4]
* Wardrip-Fruin, Noah and Pat Harrigan, eds. First Person: New Media as Story, Performance, and Game[^28]. MIT, 2004. [4]

Tags: amazon[^29] \| application program interface[^30] \| bibliography[^31] \| python[^32] \| scraping[^33] \| spidering[^34]

---

Previous: [5 Things (about Memes and the Blogosphere)](20070122-5-things-about-memes-and-blogosphere.md)  
Next: [Exploratory Bibliography 2: Visualization](20070127-exploratory-bibliography-2.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2007/01/readings-for-field-in-digital-history.html`
[^2]: `http://digitalhistoryhacks.blogspot.com/2006/09/easy-pieces-in-python-simple-scraping.html`
[^3]: `http://docs.python.org/lib/module-pickle.html`
[^4]: `http://digitalhistory.uwo.ca/dhh/hacks/exploratory-bibliography-01.py.html`
[^5]: `http://digitalhistoryhacks.blogspot.com/2006/08/easy-pieces-in-python-removing-stop.html`
[^6]: `http://digitalhistoryhacks.blogspot.com/2006/08/easy-pieces-in-python-word-frequencies.html`
[^7]: `http://digitalhistory.uwo.ca/dhh/hacks/exploratory-bibliography-02.py.html`
[^8]: `http://www.amazon.com/Long-Tail-Future-Business-Selling/dp/1401302378/`
[^9]: `http://www.amazon.com/Double-Fold-Libraries-Assault-Paper/dp/0375726217/`
[^10]: `http://www.amazon.com/Survey-Text-Mining-Clustering-Classification/dp/0387955631/`
[^11]: `http://www.amazon.com/Understanding-Search-Engines-Mathematical-Environments/dp/0898715814/`
[^12]: `http://www.amazon.com/Computer-History-Information-Machine-Technology/dp/0813342643/`
[^13]: `http://www.amazon.com/Everyware-Dawning-Age-Ubiquitous-Computing/dp/0321384016/`
[^14]: `http://www.amazon.com/Dealers-Lightning-Xerox-PARC-Computer/dp/0887309895/`
[^15]: `http://www.amazon.com/Cognition-Bradford-Books-Edwin-Hutchins/dp/0262581469/`
[^16]: `http://www.amazon.com/Natural-Language-Processing-Online-Applications/dp/1588112500/`
[^17]: `http://www.amazon.com/Fans-Bloggers-Gamers-Consumers-Digital/dp/0814742858/`
[^18]: `http://www.amazon.com/Structure-Scientific-Revolutions-Thomas-Kuhn/dp/0226458083/`
[^19]: `http://www.amazon.com/Electronic-Word-Democracy-Technology-Arts/dp/0226468852/`
[^20]: `http://www.amazon.com/Digital-Copyright-Protecting-Intellectual-Property/dp/1573928895/`
[^21]: `http://www.amazon.com/Designing-Interactions-Bill-Moggridge/dp/0262134748/`
[^22]: `http://www.amazon.com/Narrative-Virtual-Reality-Interactivity-Literature/dp/0801877539/`
[^23]: `http://www.amazon.com/Victorian-Internet-Tom-Standage/dp/0425171698/`
[^24]: `http://www.amazon.com/Plans-Situated-Actions-Human-Machine-Communication/dp/0521337399/`
[^25]: `http://www.amazon.com/Infotopia-Many-Minds-Produce-Knowledge/dp/0195189280/`
[^26]: `http://www.amazon.com/Anarchist-Library-Between-Freedom-Crashing/dp/0465089852/`
[^27]: `http://www.amazon.com/Dream-Machine-Licklider-Revolution-Computing/dp/014200135X/`
[^28]: `http://www.amazon.com/First-Person-Media-Story-Performance/dp/0262232324/`
[^29]: `http://technorati.com/tag/amazon`
[^30]: `http://technorati.com/tag/application+program+interface`
[^31]: `http://technorati.com/tag/bibliography`
[^32]: `http://technorati.com/tag/python`
[^33]: `http://technorati.com/tag/scraping`
[^34]: `http://technorati.com/tag/spidering`
