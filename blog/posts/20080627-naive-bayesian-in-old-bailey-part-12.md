# A Naive Bayesian in the Old Bailey, Part 12

_June 27, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-12.html`

Up until now, we've measured the error rates of our various learners without worrying too much about what good an error-prone machine learner actually is. By dividing the learner's responses into the four categories of hit, miss, false positive and correct negative, we can get a more nuanced picture of what it is doing when it makes a mistake. Here we look at false positives, trials that the learner mistakenly identifies as belonging to the category of interest. We start by writing a program that goes through each of the TFIDF-50 learner's responses for the various offence categories in the 1830s. It collects all of the false positives, making a note of what offence category each trial actually belongs to. The code to do this is here[^1]. We can then plot the information in a convenient form. I've decided to use pie charts.  
  
The figure below shows the results for the offence category of assault, coded as a way of breaking the peace. What happens when our learner thinks that a trial is an example of this category but it really isn't? About 38.6% of the time, the trial in question was actually categorized as indecent assault (sexual), and about 38.6% of the time it was assault with intent (also sexual). Almost 11% of the time, the trial was a case of assault with sodomitical intent, and another 8% of the trials were actually categorized as an instance of wounding. In other words, about 96% of the learner's false positive "errors" in this case were other kinds of assault. What of the trials classified as "miscellaneous - other"? One was this trial[^2], where 44 year old William Blackburn was found guilty of "unlawfully and maliciously administering to Hannah Mary Turner 6 drachms of tincture of cantharides, with intent to excite, &c." I understand that this case probably doesn't fit the definition of assault used by either Blackburn's contemporaries or by the person who coded the file. Nevertheless, it is not completely unrelated to the idea of an assault, and is exactly the kind of source that a historian could use to shed light on gender relations, sexuality, or other topics.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCnciVmALKd0UGtL5dEu4v8HwjkdGc-xJllUyo1BW0AieXctApbowlv3cqcvPeLfSaZ9pmp_57ZMNEH25e_IXlExitagJpRu7SaDf1R-2blHShIdUlY6Y-1sNcnPrEyjN_DlXXoA/s200/ob-tfidf50-1830s-fps-breakingpeace-assault.jpg)  
  
The next figure shows the false positives for fraud, categorized as a kind of deception. Seventy-two percent of the learner's false positives in this case were actually categorized as coining offences, and another 12% were actually cases of forgery. Once again, the vast majority of cases that were incorrectly identified as fraud belonged to relatively closely related offence categories. Note that these results cannot be explained by appealing to the distribution of offences in the sample as a whole. If the false positives were selected by the learner at random, we would expect most of them to be cases of larceny, which are by far the most commonly attested. Instead we see that a learner trained to recognize one kind of assault is confused by other kinds of assault, and one trained on fraud by other kinds of fraud.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDSUNKG_zO7pTcZzjb-DmN8cGaad1DJOOCRPbJnoH9a_RACb8nzO5cOlVankuE9eglGkUiLR9zdjLKYiF3ZQAwhaIt7Uh8eap1yKbF1Nw_Lcp3BkC_X0Iki7xF0fnqwQUUop1jDQ/s200/ob-tfidf50-1830s-fps-deception-fraud.jpg)  
  
A learner trained on manslaughter is mostly confused by cases of wounding and murder, as shown in the next figure.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCh4rDR-HkskjG5zxxRrjwUCz13amH_WGOp_xOnBZR14TN6V5WaQjN6MckrdDZ_8i4mrsVMCKKf2WGxVTg98EjUsl1z54flAFO3CXr0DWJiqTykLMtmMzMpwbM1KfTaoX10jcQTw/s200/ob-tfidf50-1830s-fps-kill-manslaughter.jpg)  
  
Finally we can consider a kind of theft, in this case housebreaking. If any learner were going to be confused by larceny cases, it should be one trained to recognize a type of theft. Instead, this learner is more confused by the less-frequently attested but more closely related categories of burglary and theft from place.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0ROubvOYh20U2uXaB49YhKQ2mst_rUt0aw-IwLLG_BDDwIkFWTi33V2m55TyizMccxINKxfYPDo2EuQQy2Qb8RRXNkZc4ortdRy4DS5Tl4uc7enwj-HTEVQzm9DWnoRU4FxkAgw/s200/ob-tfidf50-1830s-fps-theft-housebreaking.jpg)  
  
Now we are in a position to provide one kind of answer to the question, "what good is an error-prone learner?" Since the learner's errors are meaningfully related to its successful ability to categorize, we can use false positives as a way of generalizing beyond the bounds of hard and fast categorization. If we used a search engine to find cases of assault we might miss some of the most interesting such cases (like the cantharides example) ... cases that are interesting precisely because they lay just outside the category. One of the things that machine learning gives us, is a way of finding some of the more interesting exceptions to our rules.  
  
Tags: archive[^3] | data mining[^4] | digital history[^5] | feature space[^6] | machine learning[^7] | text mining[^8]

[Back to the blog archive](../README.md)

[^1]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-test-false-positives.py.html`
[^2]: `http://www.oldbaileyonline.org/browse.jsp?id=t18360919-2166&div=t18360919-2166`
[^3]: `http://technorati.com/tag/archive`
[^4]: `http://technorati.com/tag/data+mining`
[^5]: `http://technorati.com/tag/digital+history`
[^6]: `http://technorati.com/tag/feature+space`
[^7]: `http://technorati.com/tag/machine+learning`
[^8]: `http://technorati.com/tag/text+mining`
