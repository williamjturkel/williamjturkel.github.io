# A Naive Bayesian in the Old Bailey, Part 7

_June 17, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-7.html`

At last we're in a position to actually train and test some machine learners. The one that we'll start with is called a naive bayesian. It is relatively simple to implement, although it usually doesn't perform nearly as well as fancier and more complicated learners. For our purposes, however, it has some real advantages, which we'll get to spelling out eventually. The version of the naive bayesian learner that I am going to use is the one that was implemented by Toby Segaran in his book Programming Collective Intelligence[^1]. I won't post the code for the learner here, as it is already available online[^2]. If you are able to follow this series of posts and are interested in writing machine learning code in Python, Toby's book is a must-have. The only change that I have implemented is to remove stop words before submitting the trials for training or testing. You can get instructions and code for that from The Programming Historian[^3].  
  
Bayesian learners make use of a theorem proposed by Thomas Bayes and published in 1763, two years after his death (for more on Bayes, see Bellhouse's biography[^4].) The theorem states that Pr[H|E] = (Pr[E|H] \* Pr[H]) / Pr[E]. Pr[H|E] is the probability that the hypothesis H is true, given some evidence E. Pr[E|H] is the probability that you would see evidence E if the hypothesis H were true. Pr[H] is the probability of the hypothesis and Pr[E] the probability of the evidence. Bayes theorem gives us a way of determining conditional probabilities: if we know one thing, how likely are we to know something else?  
  
Let's work through a simple example. Suppose bag A contains one black marble and three white ones, and bag B contains two white marbles and two black ones. Someone gives us a black marble but doesn't remember which bag they took it from. Given that you have a black marble, what are the chances that it came from bag A? In this case, Pr[H] is the probability the marble came from bag A. Since each bag contains the same number of marbles, Pr[H] = 4/8 = 1/2. Pr[E] is the probability that a marble is black, so Pr[E] = (1+2)/8 = 3/8. Pr[E|H] is the probability that you are going to get a black marble if you choose from bag A, in other words Pr[E|H] = 1/4. So Bayes theorem says that Pr[H|E] = (1/4\*1/2) / 3/8 = 1/3. Since we know that the marble had to come from one of the two bags, that means that it should have a 2/3 chance of coming from bag B, which we can double check. Pr[notH|E] = (Pr[E|notH] \* Pr[notH]) / Pr[E] = (2/4\*1/2) / 3/8 = 2/3, as expected. You can learn more about Bayes theorem here[^5].  
  
When applied to the problem of learning, Bayes theorem looks like this: Pr[category|document] = Pr[document|category] \* Pr[category]. (We don't need to divide by Pr[document] in this equation because it will scale all of our results by the same amount). We make the (incorrect) assumption that the probability of each word in the document is independent from the others, so we can set Pr[document|category] equal to Pr[word1|category] \* Pr[word2|category] \* ... Finally, Pr[category] is simply the proportion of all documents that belong to our category of interest.  
  
So how well does the naive bayesian learner do? Not very well. In a tenfold cross-validation run testing for cases of simple larceny in the 1830s it has an average error rate of 39.17%, compared with COINFLIP's average error rate of 49.39%. The error rate is simply (Misses + False Positives) / Total Number of Trials. Part of the problem is that we made the assumption that the probability of any word in a document is independent of the probability of any other word in the same document. We know this isn't strictly true. In the Old Bailey proceedings, for example, you find both "dwelling" and "dwelling house", as well as "victualling house", "sessions house", "station house", "house keeper" and many other forms. To the extent that these and other words tend to co-occur, the word probabilities can't be independent. We can improve the performance of our naive bayesian learner by using pairs of words (i.e., 2-grams) rather than individual words as features for the learner. This drops the error rate to 26.23% when categorizing trials for simple larceny in the 1830s. The code that tests the different learners is here[^6]. A graph of performance is shown below.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguBpwzlLLpzI5Nr4TOPCj9tI-GLpczHZdyj52vDoF2uyULw2m8NuneABC6d_SDrPi6nN8wkBmyxTpRG9apRxlh7RpZI_2tpOIGeybGayVj39EeqDKHL7rw_9m8tCkA0DWRjoPvuA/s200/ob-cross-validation-larceny-stats.jpg)  
  
Tags: archive[^7] | data mining[^8] | digital history[^9] | feature space[^10] | machine learning[^11] | text mining[^12]

[Back to the blog archive](../README.md)

[^1]: `http://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325/`
[^2]: `http://blog.kiwitobes.com/?p=44`
[^3]: `http://niche.uwo.ca/programming-historian/index.php/Main_Page`
[^4]: `http://www.york.ac.uk/depts/maths/histstat/bayesbiog.pdf`
[^5]: `http://plato.stanford.edu/entries/bayes-theorem/`
[^6]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-cross-validate-learner.py.html`
[^7]: `http://technorati.com/tag/archive`
[^8]: `http://technorati.com/tag/data+mining`
[^9]: `http://technorati.com/tag/digital+history`
[^10]: `http://technorati.com/tag/feature+space`
[^11]: `http://technorati.com/tag/machine+learning`
[^12]: `http://technorati.com/tag/text+mining`
