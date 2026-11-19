# A Naive Bayesian in the Old Bailey, Part 4

_June 9, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-4.html`

With raw text files for each of the trials, we're almost in a position to try doing some experiments with a machine learner. Before we get started we are going to need a few utility routines to make our lives easier. Programmers enjoy writing tools so much they have a special expression for the process: yak shaving[^1]. Sometimes it's necessary, sometimes it's just fun, sometimes it's a great way to procrastinate. We'll try to keep it in check.  

* First of all, we'll want lists of all of the files that need to be processed in a given decade. We could use the operating system for this, but Windows is pretty slow when you have tens of thousands of files in a directory. A program to grab the list of filenames to another text file is here[^2].
* We're also going to want a list of all of the dates on which trials occurred (in other words, we will want a list of all of the days that the court was in session). The program to generate that list and sort it in ascending order is here[^3].
* Since our initial experiments will be focused on trying to automatically categorize trials by offence (e.g., "burglary"), we are going to need a few routines that make it easier to work with offences. One of these needs to return a mapping from trial IDs to one or more categories of offence (the code is here[^4]):

* t-18341124-1.txt -> theft-burglary
* t-18341124-2.txt -> theft-burglary
* t-18341124-3.txt -> breakingpeace-wounding
* ...
* t-18341124-37.txt -> theft-stealingfrommaster, theft-simplelarceny
* ...

* Another routine needs to return a mapping from a particular offence to a list of matching trial IDs (the code is here[^5]):

* theft-burglary -> t-18341124-1.txt, t-18341124-183.txt, t-18341124-185.txt, t-18341124-2.txt, t-18341124-4.txt, ...

* Finally, we are going to need to have some idea of how many offences there were of each kind in a particular decade (the code is here[^6]). For the 1830s, the data look like the following:

* breakingpeace-assault.txt\|51
* breakingpeace-libel.txt\|7
* breakingpeace-riot.txt\|5
* breakingpeace-threateningbehaviour.txt\|4
* breakingpeace-wounding.txt\|166
* breakingpeace.txt\|1
* damage-arson.txt\|7
* damage-other.txt\|1
* ...

That about does it for the utility routines. Next we have to address the problem of sampling.  
  
Tags: archive[^7] \| data mining[^8] \| digital history[^9] \| feature space[^10] \| machine learning[^11] \| text mining[^12]

[Back to the blog archive](../README.md)

[^1]: `http://www.catb.org/jargon/html/Y/yak-shaving.html`
[^2]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-trial-id-list.py.html`
[^3]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-get-date-range.py.html`
[^4]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-offence-category.py.html`
[^5]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-offence-index.py.html`
[^6]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-count-offences.py.html`
[^7]: `http://technorati.com/tag/archive`
[^8]: `http://technorati.com/tag/data+mining`
[^9]: `http://technorati.com/tag/digital+history`
[^10]: `http://technorati.com/tag/feature+space`
[^11]: `http://technorati.com/tag/machine+learning`
[^12]: `http://technorati.com/tag/text+mining`
