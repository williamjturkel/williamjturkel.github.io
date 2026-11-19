# Text Mining the DCB, Part 4

_February 9, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/02/text-mining-dcb-part-4.html`

In our efforts to do some simple text mining of the online Dictionary of Canadian Biography[^1], we created a list 65 distinctive features and located each of the biographies in Volume 1 in a 65-dimensional space. The next step is to figure out how far (in some sense) each of the biographies is from its neighbours.  
  
Remember that we coded the absence of a given feature as '0' and the presence as '1' for each biography. This means that we can compare any two biographies simply by lining up the corresponding values for each feature, like so (assuming, for the sake of example, that we only have six features instead of 65):  

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  
 Argall, Sir Samuel | 1 | 1 | 1 | 0 | 0 | 0 |
| Champlain, Samuel de | 1 | 0 | 1 | 1 | 0 | 1 |

  
Now we have a number of options for computing the distance between any two biographies. One possibility would be to add up the number of features that both have in common or both lack. For the example above, the two biographies share the first and third features and both lack the fifth. A simple distance measure is  
  

1-(common\_features/6)

  
  
Since these two biographies have three common features, their distance by this measure is  
  

1-(3/6) = 0.5

  
  
If two biographies had all of the same features, then their distance would be  
  

1-(6/6) = 0

  
  
which makes sense, and if they had no common features  
  

1-(0/6) = 1

  
  
This measure is applied to all of our biographies with this hack[^2]. We can then write another hack[^3] to sift through the file looking for biographies that are very close together or very far apart.  
  
Before looking at the results, it is worth trying to predict what we might find. Since our distance measure includes features that two biographies lack, one way for a pair of biographies to be close is for both to lack a lot of features. This might especially be the case for very short entries. (Another possibility, and the preferred one, would be for two biographies to match because they shared a lot of the same features. If this turns out to be the behaviour that we want, we can easily adjust our distance measure to only count shared features, and not the shared lack of features.) How might a pair of biographies be far apart? They may disagree on a lot of features, and this would be the preferred result. But it is also possible that one biography might have a lot of features because it is relatively long, and would thus differ from short ones. Again, this may or may not be interesting if it happens, and we may have to frob[^4] our distance measure.  
  
So what happens when we run the hacks? The biographies that are closest together by this measure are ones like François Bailly[^5], Mathurin Gagnon[^6], Marie-Françoise Giffard[^7], Jean Guyon du Buisson[^8], and Marie Irwin[^9]. Each is very short, confirming our suspicion that we might not want to pay so much attention to a lack of features. (As an aside, however, note that this measure pulls out the men and women who are more obscure, and thus could be useful for finding historical topics in the 'long tail'[^10].)  
  
What about the pairs of biographies that are far apart? Here we find something quite unexpected. There are two biographies that are very distant from a bunch of the others, Samuel de Champlain[^11] and Jean Talon[^12]. These two men dominate most accounts of New France. Their entries in the DCB are very long. So not only does minimizing this distance measure give us a way of approaching Canadian historical biography from below, but maximizing it allows us to sift out the 'great men'.  
  
At this point, a skeptic might say that all we have done is create a nonobvious way to estimate the length of biographical entries... the longer the entry, the more likely it is to have positive features. We can easily test this hypothesis by checking the filesizes of all of the biographies. Sure enough, Champlain's and Talon's are the longest in Volume 1. So we will want to refine our distance measure to exclude the shared lack of features, when we move to the next step of our investigation, clustering.  
  
Tags: dictionary of canadian biography[^13] | digital history[^14] | feature space[^15] | hacking[^16] | long tail[^17] | perl[^18] | text mining[^19]

[Back to the blog archive](../README.md)

[^1]: `http://www.biographi.ca/EN`
[^2]: `http://digitalhistory.uwo.ca/dhh/hacks/dcbo-distances.pl.html`
[^3]: `http://digitalhistory.uwo.ca/dhh/hacks/dcbo-minmax-dists.pl.html`
[^4]: `http://www.hacker-dictionary.com/terms/frobnicate`
[^5]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34164`
[^6]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34356`
[^7]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34373`
[^8]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34393`
[^9]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34419`
[^10]: `http://digitalhistoryhacks.blogspot.com/2006/01/historical-topics-in-long-tail.html`
[^11]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34237`
[^12]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34663`
[^13]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^14]: `http://technorati.com/tag/digital+history`
[^15]: `http://technorati.com/tag/feature space`
[^16]: `http://technorati.com/tag/hacking`
[^17]: `http://technorati.com/tag/long+tail`
[^18]: `http://technorati.com/tag/perl`
[^19]: `http://technorati.com/tag/text+mining`
