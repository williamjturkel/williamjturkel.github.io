# A Naive Bayesian in the Old Bailey, Part 9

_June 21, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-9.html`

There are many different ways to measure the performance of our various learning algorithms. The error rate that we've been using so far we defined as the sum of misses and false positives divided by the total number of trials. By this measure, COINFLIP had an average error rate around 50%, and our naive bayesian learner had an error rate around 40% using one word features, and around 26% using either 2-grams or top-scoring tf-idf features. I thought I might be able to get better performance by using only those 2-grams that included terms with a high tf-idf, but that learner had an error rate around 26%, too. (Recall that we've been using cases of simple larceny in the 1830s for our experiments... the performance will be different for other offences and/or other decades. We'll test some of these soon.)  
  
By using a different measure, we can see that our various learners achieve their results in different ways. From our perspective as researchers, the least interesting category of answers are the correct negatives. Misses are a problem, because they may contain evidence that relates to the argument that we're trying to construct. False positives are a problem, because they are irrelevant but we have to look through them to determine that... in other words, they're a waste of time. A perfect learner would return all and only hits. If we consider the ratio of misses to hits we can get an idea of how accurate our learner is. As a learner gets better, the ratio of misses to hits approaches 0. As it gets worse, the ratio increases. A disastrous learner might not get any hits, so to avoid a division by zero error, we'll add one to the denominator. Our accuracy measure is thus misses / (hits + 1). If we consider the ratio of false positives to hits we can find out how precise our learner is. As it gets better, this ratio will go to zero, and as it gets worse, the ratio will increase. Our precision measure is false positives / (hits + 1). We can plot both measures on the same graph, with the origin in the lower left hand corner, as shown below. Since some of the values are large, I've used logarithmic axes. (Also, the results for YES and NO actually lie on the respective zero lines, but I've bumped them over so they can be seen in this plot.)  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPKJAA0acoF-11O2hk8_oiXYuylH8D3LkZBYbYSi2W08mRJxgmkQuWTuLk1d-kMIh6fcI1hj4I6eCbddQk9Z7SVXSM0cmz-tDjtHvsdP12dUPCN8mizdJ11eKC9m9DIyxm0bl81Q/s200/ob-larceny-stats-2.jpg)  
  
Looking at the graph we notice some interesting results. The naive bayesian that uses words for features gets relatively few false positives, but at the cost of missing an order of magnitude more items than the other two learners. The 2-gram learner outperforms COINFLIP and the tf-idf learner on false positives, but not on misses. The tf-idf learner is the only one that outperforms COINFLIP in terms of both accuracy and precision. Thus we will do our next round of experiments with the tf-idf learner.  
  
Tags: archive[^1] \| data mining[^2] \| digital history[^3] \| feature space[^4] \| machine learning[^5] \| text mining[^6]

[Back to the blog archive](../README.md)

[^1]: `http://technorati.com/tag/archive`
[^2]: `http://technorati.com/tag/data+mining`
[^3]: `http://technorati.com/tag/digital+history`
[^4]: `http://technorati.com/tag/feature+space`
[^5]: `http://technorati.com/tag/machine+learning`
[^6]: `http://technorati.com/tag/text+mining`
