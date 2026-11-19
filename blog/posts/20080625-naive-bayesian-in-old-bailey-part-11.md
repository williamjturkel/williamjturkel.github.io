# A Naive Bayesian in the Old Bailey, Part 11

_June 25, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-11.html`

We feel pretty confident that the performance of the TFIDF-50 version of the naive bayesian learner is going to be relatively stable regardless of the frequency with which a particular offence is attested. At this point we can write a routine which tests the learner on each of the offences which occurred 10 or more times in the 1830s. Our testing routine takes advantage of the fact that, unlike many other kinds of machine learner, the naive bayesian can be operated in *online* mode. What this means is that we can train the learner on some data, test its performance, then train it on some more data. Many learners can only be operated in *offline* or *batch* mode. This means they have to be trained on all of the data before they can be tested, and there is no way at that point to subject them to further training. The fact that the naive bayesian can be used for online learning will turn out to be crucial for us.  
  
The code for testing is here[^1]. The learner is given the trials in chronological order, one at a time. The way that the program works is that it first uses the current state of the learner to classify a trial. The classification is scored as a hit, miss, false positive or correct negative, then the trial is used to train the learner (with the appropriate category being given as feedback). The learner is then given the next trial to judge. Once the learner has seen all of the data, the final count of hits, misses, etc. is output and the performance plotted as in previous posts. The results are shown below for the 1830s.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQrAjuSVayuY1YLza2Ux2n_jdj2Q1waxk0lYCkx5mIdJffk3j289X6tDh3_QWp0AmCoq83PLMSNubZM17dbjjTGVzVKKr_LqjK35IElFThxcpYndlQESHUxFUAY0x6pWS3J0W6OQ/s200/ob-tfidf50-1830s.jpg)  
  
As can be seen, the performance is pretty stable, considering that different offences make up values ranging between 0.077% (for perverting justice 10/12959) and 42.48% of the total (for simple larceny 5505/12959). The system gets very few false positives for bigamy, and quite a few for shoplifting. We'll look at why this is the case in the next post. It is very accurate for the most frequently attested offence, simple larceny, and relatively inaccurate for the infrequently attested offences of kidnapping (11/12959) and perverting justice (10/12959). The central part of the plot is magnified and shown in the figure below. The performance of the learner varies for similar sorts of crime (e.g., it performs better for indecent assault than assault), something that we will take up next.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxm01CcN74exz4jBe5iqHuVY7_nRd1iIPiPs8tKrhyphenhyphenENU7x8kQVeSkqgl7RHyfLbrTdWoteWHRLz5KE-D-lRNsJnYEJrYmgLcRqCOu0kI8O528Gv7iMhXDVmB9jjXEA7xj7iqnBg/s200/ob-tfidf50-1830s-detail.jpg)  
  
Tags: archive[^2] \| data mining[^3] \| digital history[^4] \| feature space[^5] \| machine learning[^6] \| text mining[^7]

[Back to the blog archive](../README.md)

[^1]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-online-learning.py.html`
[^2]: `http://technorati.com/tag/archive`
[^3]: `http://technorati.com/tag/data+mining`
[^4]: `http://technorati.com/tag/digital+history`
[^5]: `http://technorati.com/tag/feature+space`
[^6]: `http://technorati.com/tag/machine+learning`
[^7]: `http://technorati.com/tag/text+mining`
