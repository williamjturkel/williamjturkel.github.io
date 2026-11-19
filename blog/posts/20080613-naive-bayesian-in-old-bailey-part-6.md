# A Naive Bayesian in the Old Bailey, Part 6

_June 13, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-6.html`

Now that we have our training and testing samples, we will be able to estimate the error rates of our various machine learners. Some of them won't be very good, especially if they are trained on relatively small or unrepresentative samples. None of them will be perfect, or even approach human performance. So it is usually a good idea to ask if the performance of a given learner is significantly different from chance. Consider three other abstract machines which don't do any learning at all.  
  
YES is a very simple machine. When given an item and asked whether or not it is an instance of a particular category, YES says "yes". That's it. Suppose we have 100 test items and all of them are instances of our category, say 100 examples of burglary. We ask YES about each of them and it 'decides' that each is a burglary. YES makes no errors at all on this test sample! If half of the test items are not burglaries, however, YES's error rate climbs to 50%.  
  
NO is also a very simple machine, responding "no" whenever tested. If we give it 100 examples of burglaries, it will fail to recognize every single one of them, with an error rate of 100%. The fewer burglaries our test sample contains, the better NO does.  
  
COINFLIP is more sophisticated than YES or NO. Every time we ask COINFLIP to make a decision, it has a 50% chance of responding "yes" and a 50% chance of responding "no". Given a sample with 100 examples of burglaries, COINFLIP gets it wrong about half the time. Given a sample with no burglaries in it, COINFLIP will also have an error rate around 50%.  
  
With these three simple machines, we can be more clear about what it means to be right or wrong, distinguishing four categories:  

* Hit. If the machine says "yes" and the right answer is "yes", we say that it has scored a hit. This is one kind of correct answer. Both YES and COINFLIP are capable of scoring hits, but NO never is, because it can never say "yes" to anything.
* False Positive. If the machine says "yes" but the answer is really "no", we say that it has responded with a false positive, which is one kind of incorrect answer. YES and COINFLIP can reply with false positives, but NO cannot.
* Miss. If the machine says "no" but the correct answer was "yes", we say that it missed. NO and COINFLIP can miss, but YES cannot, because it never says "no".
* Correct Negative. This happens when the machine says "no" and the correct answer was "no". NO and COINFLIP can reply with correct negatives, but YES cannot.

We expect our learners to produce answers in each of the four categories. A machine that always hits will also tend to identify a lot of false positives. This can be good if you are looking for a needle in a haystack, but will overwhelm you if your category is well-attested. A machine that always identifies correct negatives will often miss things. These kind of machines tend to be more useful when you would never have time to go through all of your items by hand. Most machine learners have parameters that allow you to tune their performance between these extremes.  
  
Tags: archive[^1] | data mining[^2] | digital history[^3] | feature space[^4] | machine learning[^5] | text mining[^6]

[Back to the blog archive](../README.md)

[^1]: `http://technorati.com/tag/archive`
[^2]: `http://technorati.com/tag/data+mining`
[^3]: `http://technorati.com/tag/digital+history`
[^4]: `http://technorati.com/tag/feature+space`
[^5]: `http://technorati.com/tag/machine+learning`
[^6]: `http://technorati.com/tag/text+mining`
