# A Naive Bayesian in the Old Bailey, Part 14

_July 3, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/07/naive-bayesian-in-old-bailey-part-14.html`

I'm off to England next week to present some of this work at the Metropolis on Trial[^1] conference, so it is time to bring this series of posts to a close. I'd like to wrap up by summarizing what we've accomplished and making a clearer case for machine learning as a tool for historical research.  
  
Papers in the machine learning literature often say something like "we tested learners x, y, and z on this standard data set and found errors of 40%, 20% and 4% respectively. Learner z should therefore be used in this situation." The value of such research isn't immediately apparent to the working historian. For one thing, many of the most powerful machine learning algorithms require the learner to be given all of the training data at once. Historians, on the other hand, tend to encounter sources piecemeal, sometimes only recognizing their significance in retrospect. Training a machine learner usually requires a labelled data set: each item already has to be categorized. It's not obvious what good a machine learner is, if the researcher has to do all the work in advance. Finally, there is the troublesome matter of errors. What good is a system that screws up one judgement in ten? Or one in four?  
  
In this work we considered a situation that is already becoming familiar to historians. You have access to a large archive of sources in digital form. These may consist of raw OCR text (full of errors), or they may be edited text, or, best of all, they may be marked up with XML, as in the case of the Old Bailey trials. Since most of us are not lucky enough to work with XML-tagged sources very often, I stripped out the tags to make my case more strongly.  
  
Now suppose you know exactly what you're looking for, but no one has gone through the sources yet to create an index that you can use. In a traditional archive, you might be limited to starting at the beginning and plowing through the documents one at a time, skimming for whatever you're interested in. If your archive has been digitized you have another option. You can use a traditional search engine to index the keywords in the documents. (You could, for example, download them all to your own computer and index them with Google Desktop[^2]. Or you could get fancy with something like Lucene[^3].) Unless your topic has very characteristic keywords, however, you will be getting a mix of relevant and irrelevant results with every search. Under many conditions, a keyword search is going to return hundreds or thousands of hits, and you are back to the point of going through them one at a time.  
  
Suppose you're interested in larceny. (To make my point, I'm picking a category that the OB team has already marked up, but the argument is valid for anything that you or anyone else can reliably pick out. You might be studying indirect speech, or social deference, or the history of weights and measures. As long as you can look at each document and say "yes, I'm interested in this" or "no, I'm not interested in this" you can use this technique.) Anyway, you start with the first trial of 24 Nov 1834. It is a burglary, so you throw it in the "no" pile. The next record is a burglary, the third is a wounding, and so on. After you skim through 1,000 trials, you've found 444 examples of larceny and 556 examples of trials that weren't larceny. If you kept track of how long it took you to go through those thousand trials, you can estimate how long it will take for you to get through the remaining 11,959 trials in the 1830s, and approximately how many more cases of larceny you are likely to find. But you're less than a tenth of the way through the decade's trials, and no further ahead on the remaining ones.  
  
Machine learning gives you a very powerful alternative, as we saw in this series. The naive bayesian learner isn't the most accurate or precise one available, but it has a couple of enormous advantages for our application. First of all, it is relatively easy to understand and to implement. Although we didn't make use of this characteristic, it is also possible to stop the learner at any point and find out which features it thinks are most significant. Second, the naive bayesian is capable of incremental learning. We can train it with a few labelled items, then test it on some unlabelled items, then train it some more. Let's go back to the larceny example. Suppose as you look at each of the thousand trials, you hand it off to your machine learner along with the label that you've assigned. So once you decide the first trial is a burglary, you give it to the learner along with the label "no". (This doesn't have to be laborious... the process could easily be built into your browser, so as you review a document, you can click a plus or minus button to label it for your learner.) Where are you after 1,000 trials? Well, you've still found your 444 examples of larceny and your 556 examples of other offence categories. But at this point, you've also trained a learner that can look through the next 11,959 trials in a matter of seconds and give you a pile containing about 2,500 examples of larceny and about 750 false positives. That means that the next pile of stuff that you look through has been "enriched" for your research. Only 44% of the first thousand trials you looked at were examples of larceny. Almost 77% of the next three thousand trials you look at will be examples of larceny, and the remaining 23% will be more closely related offences. Since the naive bayesian is capable of online learning, you can continue to train it as you look through this next pile of data.  
  
Machine learning can be a powerful tool for historical research because  

1. It can learn as a side effect of your research process at very little cost to you
2. You can stop the system at any point to see what it has learned, getting an independent measure of a concept of interest
3. You can use it at any time to "look ahead" and find items that it thinks that you will be interested in
4. Its false positive errors are often instructive, giving you a way of finding interesting things just beyond the boundaries of your categories
5. A change in the learner's performance over time might signal a historically significant change or discontinuity in your sources

Tags: archive[^4] | data mining[^5] | digital history[^6] | feature space[^7] | machine learning[^8] | text mining[^9]

[Back to the blog archive](../README.md)

[^1]: `http://metropolisontrial.wordpress.com/`
[^2]: `http://desktop.google.com/features.html`
[^3]: `http://lucene.apache.org/`
[^4]: `http://technorati.com/tag/archive`
[^5]: `http://technorati.com/tag/data+mining`
[^6]: `http://technorati.com/tag/digital+history`
[^7]: `http://technorati.com/tag/feature+space`
[^8]: `http://technorati.com/tag/machine+learning`
[^9]: `http://technorati.com/tag/text+mining`
