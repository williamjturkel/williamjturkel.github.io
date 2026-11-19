# A Naive Bayesian in the Old Bailey, Part 13

_July 1, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/07/naive-bayesian-in-old-bailey-part-13.html`

So far, we've only been working with the Old Bailey trials of the 1830s, almost thirteen thousand in total. It would be nice to know if our learner continues to perform well as we give it more testing data. In the following runs, I trained a TFIDF-50 learner for each offence category that was attested more than 10 times in the 1830s. The training data consisted of all of the trials from the decade, labelled and presented to the learner in chronological order. Training was then stopped, and each learner was tested on the 25,403 unlabelled trials of the 1840s, also presented in chronological order. In order to assess the learners' performance, I used the same measures that we developed earlier, comparing the ratio of misses to hits (accuracy) and the ratio of false positives to hits (precision). As before, I added one to the denominator, so as not to accidentally divide by zero. (Computers hate it when you do that.)  

The results for the accuracy measure are shown below, in the form of a bar graph rather than the scatterplot-style figure we used before. In this graph and the next one, we can see that the performance of the learner is about as good for data that it hasn't seen (i.e., the 1840s trials) as it is for the data that were used to train it. Most of the measures are around two or less, which is comparable to what we saw before[^1]. The performance has actually improved for many of the offence categories, like assault, fraud, perjury, conspiracy, kidnapping, receiving and robbery. We do notice, however, some performance degradation for a number of sexual offences, including sexual assault with sodomitical intent, bigamy, indecent assault, rape and sodomy. This might be a statistical anomaly. On the other hand, it might be a sign that the language that was used to describe sexual offences changed somewhat in the 1840s, causing a learner trained on 1830s data to miss later cases. This is one of the ways that tools like machine learning can be used to generate new research questions.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0f-_zc96DgwBb51AArkO173wJA_4YpT5XvLOs1NRSDPsyVCbTtegD1lWdPALllsmflbAjY4kNqc7t7Zw3BSJarPDoVfPhUAk2gl7PKPuuRkfWt7gyHYtliS2DqKWG37mJKRDppw/s200/ob-tfidf50-1830s-40s-missratio.jpg)  

The next figure shows the results for the precision measure. In general the learner makes more false positive errors than misses, which is exactly what we want, given that the false positives can be useful in themselves[^2]. We don't see quite the same clear difference between sexual and non-sexual offence categories that we saw with the accuracy measure ... and for some reason it is quite hard for our learner to pick out cases of perverted justice in the 1840s.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCwYdRTNWymf6a80R1oojlPApSBAnZfX9EIfpHNMBFh6ac5CfLIiauyiVfBmS3_eRjVcxbxmEDZ91h3oZtqotx5dAqLGmD2WxxG-625gKv5AzFZYIwzk1YH8I_2Zy1zNw8L9mhpw/s200/ob-tfidf50-1830s-40s-fpratio.jpg)  

Tags: archive[^3] \| data mining[^4] \| digital history[^5] \| feature space[^6] \| machine learning[^7] \| text mining[^8]

---

Previous: [A Naive Bayesian in the Old Bailey, Part 12](20080627-naive-bayesian-in-old-bailey-part-12.md)  
Next: [A Naive Bayesian in the Old Bailey, Part 14](20080703-naive-bayesian-in-old-bailey-part-14.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-11.html`
[^2]: `http://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-12.html`
[^3]: `http://technorati.com/tag/archive`
[^4]: `http://technorati.com/tag/data+mining`
[^5]: `http://technorati.com/tag/digital+history`
[^6]: `http://technorati.com/tag/feature+space`
[^7]: `http://technorati.com/tag/machine+learning`
[^8]: `http://technorati.com/tag/text+mining`
