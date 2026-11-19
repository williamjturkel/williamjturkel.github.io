# Text Mining the DCB, Part 3

_February 4, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/02/text-mining-dcb-part-3.html`

Last week we began the process of text mining the online *Dictionary of Canadian Biography[^1]*. We created local HTML and text copies of each of the 592 biographical entries in Volume 1. We also passed the text copies through a commercial concordancing program to determine which words occurred most frequently. Once we threw out the words that were too common to provide much useful information ('the', 'a', 'and', etc.), we were left with a set of words which will potentially convey interesting and distinctive information about the biographies in Volume 1. A list of these words is in the following text file[^2].  
  
We can think of each of these words as a dimension in a highly multidimensional space. This is not immediately intuitive, so it helps to work up to the idea with simpler examples. Suppose we have two people, Samuel de Champlain[^3] and Sir Samuel Argall[^4]. In Champlain's biography, it mentions Montreal, but in Argall's biography it does not. If every biography that mentions Montreal is coded with a '1' and every biography that doesn't is coded with a '0', then we have a one-dimensional space. Every biography in this space will either be located at '0' or '1'. In fact, 196 of the 592 biographies in Volume 1 do mention Montreal, and the other 396 do not. In some sense, we want to say that those biographies that do mention Montreal are closer to one another (at least along that dimension) than the ones that do not.  
  
But what if we take another word into account, like "Jesuit(s)"? We now have two dimensions and four possibilities: a biography might mention both Montreal and Jesuit(s), it might mention one but not the other, or it might mention neither. In fact, Jesuits are mentioned in both Champlain's and Argall's biographies. Neither Montreal nor Jesuits are mentioned in the biography of John Abraham[^5], however.  
  
In some sense, again, we would like to say that the biography of Champlain is a bit closer to that of Argall (from which it differs along one dimension) than it is to that of Abraham (from which it differs along two dimensions). We would also like to say that Argall's biography is the same distance from each of the other two. This is shown in the following table.  
  

|  |  |  |
| --- | --- | --- |
| *Name* | *Jesuit(s)* | *Montreal* |
| Abraham, John | 0 | 0 |
| Argall, Sir Samuel | 1 | 0 |
| Champlain, Samuel de | 1 | 1 |

  
  
We can go on adding words in this fashion, each becoming a dimension along which biographies can differ. (It becomes hard to visualize these dimensions once you have more than three, of course).  
  
Given the biographies that we already downloaded and the 65 words in our text file, we can write a short hack[^6] to create a 65-dimensional feature space and locate each biography within it. We output the results as a spreadsheet[^7].  
  
Next we will want to formalize the idea of distances in our feature space...  
  
Tags: concordance[^8] | dictionary of canadian biography[^9] | digital history[^10] | feature space[^11] | hacking[^12] | perl[^13] | text mining[^14]

[Back to the blog archive](../README.md)

[^1]: `http://www.biographi.ca/EN`
[^2]: `http://digitalhistory.uwo.ca/dhh/hacks/dcbo-vol1-features.txt`
[^3]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34237`
[^4]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34149`
[^5]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34123`
[^6]: `http://digitalhistory.uwo.ca/dhh/hacks/dcbo-features.pl.html`
[^7]: `http://digitalhistory.uwo.ca/dhh/hacks/dcbo-vol1-featurespace.csv`
[^8]: `http://technorati.com/tag/concordance`
[^9]: `http://technorati.com/tag/dictionary+of+canadian+biography`
[^10]: `http://technorati.com/tag/digital+history`
[^11]: `http://technorati.com/tag/feature space`
[^12]: `http://technorati.com/tag/hacking`
[^13]: `http://technorati.com/tag/perl`
[^14]: `http://technorati.com/tag/text+mining`
