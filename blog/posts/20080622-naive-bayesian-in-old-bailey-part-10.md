# A Naive Bayesian in the Old Bailey, Part 10

_June 22, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-10.html`

In our last post, we settled on a style of plotting that shows both how accurate our learner is (i.e., does it miss very often?) and how precise (i.e., how often does it return a false positive?) We also decided to do experiments with the version of the naive bayesian learner that uses the items with the highest tf-idf as features. Our experiments to date have used the category of simple larceny in the 1830s. This offence is very well-attested, making up about 42.5% of the trials (5505/12959). At this point, we can try the performance of the same learner on offence categories that are less frequent: stealing from master (1718/12959, approx. 13.3%) and burglary (279/12959, approx 2.2%). We've been using the 15 terms with the highest tf-idf, but we should try some other values for that parameter, too. A graph for the three different offence categories is shown below. The four learners use the top scoring 15, 30, 50 and 100 items, respectively.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3iXwQVfTt8mUpRCajLRtiiJdtCc9En0j4n340ISeJd5rmoV5HFAXNbv1SdnSK_SuuKC6yCqoB4f718kSaQwI-9OetniVxfie8ObbrpBctW-xcQnbHjC1Gv24l2IKiiRnj3HPMpQ/s200/ob-tfidf-comparison.jpg)  

From the graph, it is pretty clear that it is easiest to learn to categorize larceny, which is the best-attested offence we looked at. We can also see that the TFIDF-15 learner does particularly poorly by missing many instances of the less frequent offences. Increasing the number of features the learner can make use of seems to improve performance up to a point. After that, increasing features increases the number of false positives the learner makes. We want the performance of our learner to be relatively robust when learning offence categories that are more or less frequently attested, which means we want the learner with the tightest grouping of results for these test categories (in other words, TFIDF-50).  

Note that in this test, we only ran each learner once on each data set, rather than doing ten-fold cross-validation. Our experiments with cross-validation[^1] suggested that the different versions of the learner were relatively insensitive to the order in which training and testing trials were presented. Since this is exploratory work, we will make the (possibly incorrect) assumption that a single trial is probably representative. This will let us do a lot more testing in the same amount of time.  

Tags: archive[^2] \| data mining[^3] \| digital history[^4] \| feature space[^5] \| machine learning[^6] \| text mining[^7]

---

Previous: [A Naive Bayesian in the Old Bailey, Part 9](20080621-naive-bayesian-in-old-bailey-part-9.md)  
Next: [A Naive Bayesian in the Old Bailey, Part 11](20080625-naive-bayesian-in-old-bailey-part-11.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-7.html`
[^2]: `http://technorati.com/tag/archive`
[^3]: `http://technorati.com/tag/data+mining`
[^4]: `http://technorati.com/tag/digital+history`
[^5]: `http://technorati.com/tag/feature+space`
[^6]: `http://technorati.com/tag/machine+learning`
[^7]: `http://technorati.com/tag/text+mining`
