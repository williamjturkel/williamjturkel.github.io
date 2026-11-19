# A Naive Bayesian in the Old Bailey, Part 5

_June 12, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-5.html`

With most of our support routines in place, we need to think about the problem of training a machine learner and then assessing its performance. A human being has already gone through each of the trials and assigned one or more offence categories to it:  

* this trial[^1] is a burglary, which is a kind of theft
* this trial[^2] is also a burglary
* this trial[^3] is a wounding, which is a way of breaking the peace
* ...

So we can give each raw trial to our learner and ask it to decide what offence category the trial belongs to, then we can check our learner's answer against the human-assigned category. If we do enough of these trials, we can get a precise sense of how good our learner is.  
  
Most machine learning researchers use a *holdout method* to test the performance of their learning algorithms. They use part of the data to train the system, then test its performance on the remaining part, the part that wasn't used for training. Items are randomly assigned to either the training or the testing pile, with the further stipulation that both piles should have the same distribution of examples. Since burglaries made up about 2.153% (279/12959) of the trials in the 1830s, we want burglaries to make up about two percent of the training data and about two percent of the test data. It would do us no good for all of the burglaries to end up in one pile or the other.  
  
But how do we know whether the results that we're seeing are some kind of fluke? We use cross-validation. We randomly divide our data into a number of piles (usually 10), making sure that the category that we are interested in is uniformly distributed across those piles. Now, we set aside the first pile and use the other nine piles to train our learner. We then test it on the first pile and record its performance. We then set aside the second pile for testing, and use the other nine piles for training a new learner. And so on, until each item has been used both for testing and for training. We can then average the ten error estimates. There are many other methods in the literature, of course, but this one is fairly standard.  
  
Code to create a tenfold cross-validation sample from our data is here[^4]. As a check, we'd also like to make sure that our offence category is reasonably distributed across our sample (code for that is here[^5]).  
  
Tags: archive[^6] \| data mining[^7] \| digital history[^8] \| feature space[^9] \| machine learning[^10] \| text mining[^11]

[Back to the blog archive](../README.md)

[^1]: `http://www.oldbaileyonline.org/browse.jsp?div=t18341124-1`
[^2]: `http://www.oldbaileyonline.org/browse.jsp?div=t18341124-2`
[^3]: `http://www.oldbaileyonline.org/browse.jsp?div=t18341124-3`
[^4]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-tenfold-crossvalidation-sample.py.html`
[^5]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-count-offence-instances.py.html`
[^6]: `http://technorati.com/tag/archive`
[^7]: `http://technorati.com/tag/data+mining`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/feature+space`
[^10]: `http://technorati.com/tag/machine+learning`
[^11]: `http://technorati.com/tag/text+mining`
