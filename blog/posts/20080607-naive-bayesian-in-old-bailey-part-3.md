# A Naive Bayesian in the Old Bailey, Part 3

_June 7, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/06/naive-bayesian-in-old-bailey-part-3.html`

At this point, we have a directory that contains one file for each trial in a given decade. There are a lot of these files (almost 13,000 for the 1830s alone) and each trial is still marked up with XML. In the next step we're going to create parallel directories that contain trial files with all of the XML stripped out. In other words, our trial files currently look like this:  

```xml
<trial id="t-18341124-1" n="1"><charge n="1" defid="def1-1-18341124" offenceno="1" verdictno="1"></charge><charge n="2" defid="def2-1-18341124" offenceno="1" verdictno="2"><p>1. <name role="defendant" id="def1-1-18341124" age="30" sex="m" given="JOHN" occupation="na" surname="HOLGATE"><lc>JOHN HOLGATE</lc></name> and
<name role="defendant" id="def2-1-18341124" age="27" sex="m" given="JAMES" occupation="na" surname="HOLGATE"><lc>JAMES HOLGATE</lc></name><offence n="1" ids="def1-1-18341124 def2-1-18341124"><theft category="burglary"> were indicted, for that they, on the <cd>1st of October</cd>, at <geo>St. Mary Magdalen, Bermondsey</geo>, about four o'clock in the night, the dwelling-house of <name age="na" given="JOHN" residency="st mary magdalen bermondsey" role="victim" sex="m" surname="THOMPSON">John Thompson</name>, feloniously and burglariously did break and enter...
```

and we're going to make copies that look like this:  
> 1 john holgate and james holgate were indicted for that they on the 1st of october at st mary magdalen bermondsey about four o clock in the night the dwelling house of john thompson feloniously and burglariously did break and enter...

It may seem a bit perverse to take out information that the OB team worked very hard to create, so it is probably a good idea to step back and get a broader overview of the data mining process. When writing programs to manipulate digital sources you can head down one of two paths. You can choose to explicitly encode more and more semantic (i.e., meaningful) information. This is what the OB team has done with XML markup. By using *&lt;geo>...&lt;/geo>* tags to indicate that "St. Mary Magdalen, Bermondsey" is a geographical location, they are able to provide a powerful search engine that can find places[^1]. Similarly, by indicating the age and sex of criminals and victims they make it possible for researchers to do a variety of sophisticated statistics[^2] on the archive as a whole. The downside, of course, is that this kind of explicit tagging is very labor-intensive. It is wonderful to be able to work with a digital archive that someone else has edited and marked up, but often you face a corpus of documents that is little better than raw text, or worse, that contains a high percentage of OCR[^3] errors.  

An alternative approach is to work with domain-neutral representations and algorithms. You write programs that can't tell the difference between a person's name and a place name, between English and French, or between natural language and a genomic sequence. This is closer to what traditional search engines like Google do. The downside is that you can search for text that includes the string "Bermondsey" but you can't tell Google to limit your search to geographic uses of the term. Instead your results include the neighborhood, the tube station, a local history group, a diving club, a biography, a hymn, some photos, and so on.  

Having access to text that has been semantically marked up makes it possible to create and test a wide range of powerful tools that can then be used on raw text that hasn't been marked up. For example, we know that this particular trial[^4] was for a burglary that ended with the execution of two men. Suppose we want to create a computer program which can classify trials as either "burglary" or "not a burglary." We start by creating an archive of raw text examples by stripping out the markup. We give these texts to our program, one by one, and tell it whether each text was an instance of "burglary" or not. With any luck, the program learns, somehow, to distinguish burglaries from other kinds of trial. (The details will be filled in as we go along). Now, we can test the program on other examples from this archive and get a precise sense of how well it does. If it seems to work, we can then use it to try and ferret out burglaries from other collections of untagged trial records, or even from a mass of undifferentiated search results.  

So, to create a clean copy of each of the trial files we're going to use a very brute force method. We will simply copy the file, one character at a time, skipping any characters that fall between *&lt;* and *>* inclusive. The Python code which does this job is here[^5].  

Tags: archive[^6] \| data mining[^7] \| digital history[^8] \| feature space[^9] \| machine learning[^10] \| text mining[^11]

---

Previous: [A Naive Bayesian in the Old Bailey, Part 2](20080605-naive-bayesian-in-old-bailey-part-2.md)  
Next: [A Naive Bayesian in the Old Bailey, Part 4](20080609-naive-bayesian-in-old-bailey-part-4.md)  
[Back to the blog archive](../README.md)

[^1]: `http://www.hrionline.ac.uk/ccc/forms/formMaps.jsp`
[^2]: `http://www.hrionline.ac.uk/ccc/forms/formStats.jsp`
[^3]: `http://en.wikipedia.org/wiki/Optical_character_recognition`
[^4]: `http://www.oldbaileyonline.org/browse.jsp?div=t18341124-1`
[^5]: `http://digitalhistory.uwo.ca/dhh/hacks/ob-clean-copy-trials.py.html`
[^6]: `http://technorati.com/tag/archive`
[^7]: `http://technorati.com/tag/data+mining`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/feature+space`
[^10]: `http://technorati.com/tag/machine+learning`
[^11]: `http://technorati.com/tag/text+mining`
