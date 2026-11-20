# On N-gram Data and Automated Plagiarism Checking

_October 3, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/10/on-n-gram-data-and-automated.html`

In August, Google announced that they would be releasing a massive amount of n-gram data at minimal cost (see "All Our N-gram are Belong to You[^1]").  
> We believe that the entire research community can benefit from access to such massive amounts of data. It will advance the state of the art, it will focus research in the promising direction of large-scale, data-driven approaches, and it will allow all research groups, no matter how large or small their computing resources, to play together.

In brief, an n-gram is simply a collocation of words that is n items long. "In brief" is a bigram, "a collocation of words" is a 4-gram, and so on. For more information, see my earlier post on "Google as Corpus[^2]."  

The happy day is here. For US $150 you can order the six DVD set of Google n-gram data from the Linguistic Data Consortium[^3]. While waiting for my copy to arrive, I figured that I could take this opportunity to suggest that the widespread availability of such data is going to force us to rethink the idea of plagiarism, especially the idea that plagiarism can be detected in a mechanical fashion.  

My school, for example, subscribes to a service called Turnitin. On their website, Turnitin claims that their software "Instantly identifies papers containing unoriginal material." That's a pretty catchy phrase. So catchy, in fact, that it appears, mostly unquoted, in 338 different places on the web, usually in association with the Turnitin product, but also occasionally to describe their competitors like MyDropBox.  

In the old days, say 2001, educators occasionally used Google to try and catch suspected plagiarizers. They would find a phrase that sounded anomalous in the student's written work and type it into Google to see if they could find an alternate source. I haven't heard anyone claim to have done that recently, for a pretty simple reason. Google now indexes too much text to make this a useful strategy.  

Compared with Google, Turnitin is a mewling and puking infant (N.B. allusion, not plagiarism). At best, the company can only hope for the kind of comprehensive text archive that massive search engines have already indexed. With this increase in scale, however, comes a kind of chilling effect[^4]. Imagine if your word processor warned you whenever you tried to type a phrase that someone else had already thought of. You would never write again. (Dang! That sentence has already been used 343 times. And I know that I read an essay by someone on exactly this point, but for the life of me I can't locate it to cite it.)  

What Google's n-gram data will show is that it is exceedingly difficult to write a passage that doesn't include a previously-used n-gram. To demonstrate this, I wrote a short Python script that breaks a passage of text into 5-grams and submits each, in turn, to Google to make sure that it doesn't already appear somewhere on the internet.  

My university's *Handbook of Academic and Scholarship Policy* includes the following statement, which provides a handy test case.  
> NOTE: The following statement on Plagiarism should be added to course outlines:  
> “Plagiarism: Students must write their essays and assignments in their own words. Whenever students take an idea, or a passage from another author, they must acknowledge their debt both by using quotation marks where appropriate and by proper referencing such as footnotes or citations. Plagiarism is a major academic offence (see Scholastic Offence Policy in the Western Academic Calendar).”

Here are the number of times that various 5-grams in this statement have been used on the web, sorted by frequency:  
> 5740 "should be added to course"  
> 1530 "idea or a passage from"  
> 1480 "assignments in their own words"  
> 1400 "where appropriate and by proper"  
> 1380 "or a passage from another"  
> 1270 "an idea or a passage"  
> 1120 "and assignments in their own"  
> 0923 "plagiarism is a major academic"  
> 0774 "a passage from another author"  
> 0769 "essays and assignments in their"  
> 0704 "students must write their essays"  
> 0635 "they must acknowledge their debt"  
> 0628 "must write their essays and"  
> 0619 "write their essays and assignments"  
> 0619 "marks where appropriate and by"  
> 0606 "acknowledge their debt both by"  
> 0605 "is a major academic offence"  
> 0596 "both by using quotation marks"  
> 0595 "appropriate and by proper referencing"  
> 0588 "policy in the western academic"  
> 0585 "and by proper referencing such"  
> 0585 "referencing such as footnotes or"  
> 0585 "scholastic offence policy in the"  
> 0583 "must acknowledge their debt both"  
> 0579 "by using quotation marks where"  
> 0573 "such as footnotes or citations"  
> 0572 "proper referencing such as footnotes"  
> 0570 "using quotation marks where appropriate"  
> 0561 "their debt both by using"  
> 0553 "take an idea or a"  
> 0549 "debt both by using quotation"  
> 0549 "in the western academic calendar"  
> 0548 "see scholastic offence policy in"  
> 0546 "offence policy in the western"  
> 0544 "quotation marks where appropriate and"  
> 0503 "by proper referencing such as"  
> 0492 "their essays and assignments in"  
> 0490 "note the following statement on"  
> 0479 "in their own words whenever"  
> 0453 "whenever students take an idea"  
> 0452 "from another author they must"  
> 0442 "students take an idea or"  
> 0432 "another author they must acknowledge"  
> 0389 "citations plagiarism is a major"  
> 0385 "their own words whenever students"  
> 0377 "passage from another author they"  
> 0373 "own words whenever students take"  
> 0368 "or citations plagiarism is a"  
> 0366 "footnotes or citations plagiarism is"  
> 0366 "a major academic offence see"  
> 0355 "as footnotes or citations plagiarism"  
> 0353 "the following statement on plagiarism"  
> 0348 "major academic offence see scholastic"  
> 0338 "offence see scholastic offence policy"  
> 0333 "academic offence see scholastic offence"  
> 0179 "plagiarism students must write their"  
> 0096 "plagiarism should be added to"  
> 0066 "following statement on plagiarism should"  
> 0062 "be added to course outlines"  
> 0033 "statement on plagiarism should be"  
> 0030 "on plagiarism should be added"

Beyond the mechanical, there are a lot of murky conceptual problems with plagiarism. To claim that the core value of scholarship has always been to respect the property rights of the individual author is wildly anachronistic. (For a more nuanced view, see Anthony Grafton's *Forgers and Critics*[^5] and *Defenders of the Text*[^6].) A simpleminded notion of plagiarism also makes it difficult to explain any number of phenomena we find in the actual (as opposed to normative) world of text: Shakespeare, legal boilerplate, folktales, oral tradition, literary allusions, urgent e-mails about Nigerian banking opportunities and phrases like "all our n-gram are belong to you."  

In a 2003 article[^7] in the *AHR*, Roy Rosenzweig wrote about the difficulties that historians and other scholars will face as they move from a culture of scarcity to one of abundance. In many ways, this transition has already occurred. It's time to stop pretending that prose must always be unique, or that n-grams can be property. All your prose are belong to us.[^8]  

Tags: Google[^9] \| n-grams[^10] \| pedagogy[^11] \| property rights[^12]

---

Previous: [No 'Secret Syllabus' for Digital History](20060928-no-secret-syllabus-for-digital-history.md)  
Next: [Zotero Beta Launched](20061006-zotero-beta-launched.md)  
[Back to the blog archive](../README.md)

[^1]: `http://googleresearch.blogspot.com/2006/08/all-our-n-gram-are-belong-to-you.html`
[^2]: `http://digitalhistoryhacks.blogspot.com/2006/08/google-as-corpus.html`
[^3]: `http://www.ldc.upenn.edu/Catalog/CatalogEntry.jsp?catalogId=LDC2006T13`
[^4]: `http://en.wikipedia.org/wiki/Chilling_effect`
[^5]: `http://www.amazon.com/Forgers-Critics-Creativity-Duplicity-Scholarship/dp/0691055440/`
[^6]: `http://www.amazon.com/Defenders-Text-Traditions-Scholarship-1450-1800/dp/0674195450/`
[^7]: `http://chnm.gmu.edu/resources/essays/scarcity.php`
[^8]: `http://en.wikipedia.org/wiki/All_your_base_are_belong_to_us`
[^9]: `http://technorati.com/tag/Google`
[^10]: `http://technorati.com/tag/ngrams`
[^11]: `http://technorati.com/tag/pedagogy`
[^12]: `http://technorati.com/tag/property+rights`
