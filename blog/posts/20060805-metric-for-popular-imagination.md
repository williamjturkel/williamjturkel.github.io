# A Metric for the Popular Imagination

_August 5, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/metric-for-popular-imagination.html`

In a paper that I'm currently revising for publication, I introduced the idea of fetishism as a category of analysis in the social sciences by referring to the popular idea of a fetish. One of the volume editors asked me for evidence to back up my claim. How do we know which ideas are popularly held? Surveys, maybe, but it doesn't make sense to do one in this case and my sample size would be far too small anyway.  
  
After some reflection, I realized that I could provide evidence about popular notions of fetishism by ~~surfing for porn~~ doing some statistical linguistics. In "Automatic Meaning Discovery Using Google[^1]," Rudi Cilibrasi and Paul Vitanyi provide a metric they call the Normalized Google Distance (NGD). The basic idea is straightforward although the underlying math is deep. If you have two search terms like 'cat' and 'mouse', then each of those terms will appear on some number of pages, and a smaller number of pages will contain both 'cat' and 'mouse'. Intuitively, we expect to find 'cat' with 'mouse' more frequently than 'cat' with 'louse'. The NGD formalizes this idea by providing a measure of how far apart particular terms are in conceptual space.  
  
Time for a hack[^2]. I wrote a simple Perl script that uses the Google Search API[^3] to calculate the NGD for a pair of terms.  
  
Using this tool, we can provide a measure for the distance between the term 'fetish' and some popular and scholarly associations. (Lower numbers mean the terms are more closely associated.)  
  

|  |  |
| --- | --- |
| latex | 0.356331874622984 |
| heels | 0.421554691152762 |
| gag | 0.497568478291903 |
| choke | 0.549934320808182 |
| rubber | 0.553427573822638 |
| leather | 0.57443530297729 |
| doll | 0.581254531681847 |
| dungeon | 0.604959474281258 |
| handcuffs | 0.621969750564945 |
| smoking | 0.629600508128091 |
| balloon | 0.648364151347237 |
| cigar | 0.715386689730539 |
| fur | 0.787872974829155 |
| freud | 0.792196156666702 |
| psychoanalysis | 0.797465589884342 |
| marx | 0.8195787086072 |
| krafft-ebing | 0.955885248436093 |
| commodity | 1.00639028092102 |

  
  
At this point Google really does constitute what John Battelle called "the database of intentions[^4]." More about Google in my next post...  
  
Update (26 Aug 2006): Nicolás Quiroga translated this post into Spanish for his new digital history blog Tapera[^5].  
  
Tags: application program interface[^6] | data mining[^7] | feature space[^8] | statistical natural language processing[^9]

[Back to the blog archive](../README.md)

[^1]: `http://www.arxiv.org/PS_cache/cs/pdf/0412/0412098.pdf`
[^2]: `http://digitalhistory.wikispot.org/DHH20060805-01`
[^3]: `http://www.google.com/apis/`
[^4]: `http://battellemedia.com/archives/000063.php`
[^5]: `http://tapera.php1h.com/`
[^6]: `http://technorati.com/tag/application+program+interface`
[^7]: `http://technorati.com/tag/data+mining`
[^8]: `http://technorati.com/tag/feature space`
[^9]: `http://technorati.com/tag/statistical+natural+language+processing`
