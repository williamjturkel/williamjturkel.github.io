# A Naive Bayesian in the Old Bailey, Part 2

_June 5, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-2.html`

After downloading the XML-tagged files for the nineteenth century to our local machine, we ended up with a directory tree that looks like this:  

* Tagged\_final (944 files, 9 folders)

* Tagged\_1830s\_Files (62 files)

* T18341124NW\_SUP\_DONE.xml
* T18341205PH.xml
* ...
* T18391216CLR.xml

* Tagged\_1840s\_Files (120 files)
* ...
* Tagged\_1910s\_Files (41 files)

* T19100111GS\_SUP\_DONE.xml
* T19100208GS.xml
* ...
* T19130401CLR.xml

Each XML file contains all of the trials that were conducted in a particular session. The file 'T18341124NW\_SUP\_DONE.xml', for example, is the record for 24 Nov 1834. I'm assuming that the string that follows the date in the filename ('NW\_SUP\_DONE') refers to the encoding process, so I'm going to ignore it.  
  
The next step is to split each of these XML files into individual trials. Our overall strategy will be as follows. First we want to create a directory for the trial files if one doesn't already exist. Then we will get a list of all of the XML files for the decade and step through them one at a time. For each XML file, we're going to extract each trial and save it as a separate file. Since a given trial is delimited with tags that look like <trial id="t-18341124-1" n="1"> ... </trial>, we can parse it out and save it separately as 't-18341124-1.txt'. You can read this trial[^1] online at the Old Bailey archives. You can also have a look at the XML file[^2] to see what we're dealing with. The fact that the OB team provides XML makes this archive an awesome resource for digital historians, and other online sites should do the same forthwith.  
  
There are a variety of ways to parse XML, but it is quick and easy to use the Beautiful Soup[^3] library for Python. The program that splits the XML files into separate trial files is here[^4]; for more information about using Beautiful Soup see The Programming Historian[^5]. There are far more trial files than session files: there were 12,959 trials in the 1830s alone. Now that we have one file for each trial, we're ready for the next step.  
  
Tags: archive[^6] | data mining[^7] | digital history[^8] | feature space[^9] | machine learning[^10] | text mining[^11]

[Back to the blog archive](../README.md)

[^1]: `http://www.oldbaileyonline.org/browse.jsp?div=t18341124-1`
[^2]: `http://www.oldbaileyonline.org/browse.jsp?path=sessionsPapers/18341124.xml&div=t18341124-1&xml=yes`
[^3]: `http://www.crummy.com/software/BeautifulSoup/`
[^4]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-split-into-trials.py.html`
[^5]: `http://niche.uwo.ca/programming-historian/`
[^6]: `http://technorati.com/tag/archive`
[^7]: `http://technorati.com/tag/data+mining`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/feature+space`
[^10]: `http://technorati.com/tag/machine+learning`
[^11]: `http://technorati.com/tag/text+mining`
