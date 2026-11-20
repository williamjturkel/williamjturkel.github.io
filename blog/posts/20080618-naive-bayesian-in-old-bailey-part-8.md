# A Naive Bayesian in the Old Bailey, Part 8

_June 18, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-8.html`

In the last post, we got a naive bayesian learner working and used it to categorize some Old Bailey trials from the 1830s as examples of larceny (or not). Our initial version of the learner was easy to implement, but it made the unrealistic assumption that the probabilities of particular words appearing in the text of a trial were independent. That greatly simplified computation at the cost of performance. Our initial learner had an error rate around 40%. We then revised it to use 2-grams as features rather than individual words. This captured some of the dependency between words, improving our average error rate so it was close to 25%.  

An alternative approach is to try and concentrate on the words in a trial which are most representative of a particular category. Without specifying these words in advance, we can make the assumption that they will be relatively frequent in the document in question, but relatively infrequent in the overall corpus of documents. One common measure for this is known as tf-idf[^1]. Rather than handing all of the words in a given trial to our learner, or all except the stop words, we will only hand off the 15 or 20 with the highest tf-idf. There are many different ways to compute this measure. The version that I used is tfidf = log(tf+1.0) \* log(numdocs/df), where tf is the number of times the word occurs in a particular text, numdocs is the total number of documents, and df is number of documents that the word appears in. The word "cellar," for example, appears in this trial[^2] seventeen times, and in 221 other trials in the 1830s. The tfidf for this word in this trial is log(17+1) \* log(12959/221) = 11.76781.  

To compute the tf-idf, we first need to create a list of every word that was used in all of the trials, and the number of different trials in which each word appears. We could put this information in a text file, but the file would be huge and very slow to access. Instead, we will store our document frequencies in a SQLite[^3] database, using Python commands to store and retrieve the information. The code which creates this database is here[^4]. We can then compute the tf-idf scores for each word in a given trial, creating a new directory to store these files. The code to do that is here[^5]. Finally, we will want a version of our tenfold cross-validation routine to test the performance of a naive bayesian learner that operates across tf-idf vectors rather than raw words or 2-grams (here[^6]). This new learner has similar performance to the 2-gram version, with an average error rate of 25.73% when using the 15 highest scoring tf-idf terms to categorize cases of larceny in the 1830s. As a bonus, it is remarkably fast. At this point, you're probably wondering what good a machine learner is, if one quarter of its judgments are incorrect. We'll get there.  

Tags: archive[^7] \| data mining[^8] \| digital history[^9] \| feature space[^10] \| machine learning[^11] \| text mining[^12]

---

Previous: [A Naive Bayesian in the Old Bailey, Part 7](20080617-naive-bayesian-in-old-bailey-part-7.md)  
Next: [A Naive Bayesian in the Old Bailey, Part 9](20080621-naive-bayesian-in-old-bailey-part-9.md)  
[Back to the blog archive](../README.md)

[^1]: `http://en.wikipedia.org/wiki/Tfidf`
[^2]: `http://www.oldbaileyonline.org/browse.jsp?div=t18341124-1`
[^3]: `http://www.sqlite.org/`
[^4]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-compute-doc-freqs.py.html`
[^5]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-compute-tfidf.py.html`
[^6]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-cross-validate-tfidf-learner.py.html`
[^7]: `http://technorati.com/tag/archive`
[^8]: `http://technorati.com/tag/data+mining`
[^9]: `http://technorati.com/tag/digital+history`
[^10]: `http://technorati.com/tag/feature+space`
[^11]: `http://technorati.com/tag/machine+learning`
[^12]: `http://technorati.com/tag/text+mining`
