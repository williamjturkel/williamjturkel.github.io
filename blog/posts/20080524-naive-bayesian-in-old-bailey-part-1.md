# A Naive Bayesian in the Old Bailey, Part 1

_May 24, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/05/naive-bayesian-in-old-bailey-part-1.html`

One of the great benefits of having a blog has been that people who are interested in digital history find me and let me know what they are doing in the field. For a couple of years now, I've enjoyed an intermittent but invariably thought-provoking correspondence with Tim Hitchcock[^1], one of the creators of the wonderful digital archive of the Old Bailey[^2] proceedings. The OB team has recently added records for the period from 1834 to 1913, resulting in a total of almost 200,000 trial records, all tagged with XML. When Tim offered me access to the XML files for a data mining project a few months ago, I jumped at the chance. This is still very much work in progress, but I've decided to blog about the process for others who are interested in doing similar things, whether with the Old Bailey archive or some other.  
  
I started by downloading local copies of all of the files. This is usually a good idea both because it makes the processing faster and because you aren't hammering the archive's servers every time you need to access a record. There are a number of different ways to do something like this, and it is very handy for historians to be familiar with at least some of them. One possibility is to use a Firefox extension like DownThemAll[^3]. This allows you to download all of the links or images in a webpage. It also allows you to pause and resume the download process, which can be useful when you're working with a large number of files. For those who are more comfortable with scripting and prefer command line tools, it is hard to beat GNU Wget[^4]. Both programs are free. The third alternative is to write your own script in a language like Python or Perl. This option is most difficult, but gives you more control over various kinds of preprocessing, like dealing with accented characters. (For more, see the section on this in The Programming Historian[^5].) It takes a while to download a large batch of files, but once you have them you're ready to move on to the next step.  
  
Tags: archive[^6] \| data mining[^7] \| digital history[^8] \| feature space[^9] \| machine learning[^10] \| text mining[^11]

[Back to the blog archive](../README.md)

[^1]: `http://perseus.herts.ac.uk/uhinfo/schools/humanities/hist/history-staff/tim-hitchcock.cfm`
[^2]: `http://www.oldbaileyonline.org`
[^3]: `http://www.downthemall.net/`
[^4]: `http://www.gnu.org/software/wget/`
[^5]: `http://niche.uwo.ca/programming-historian/index.php/Harvesting_links_and_downloading_pages`
[^6]: `http://technorati.com/tag/archive`
[^7]: `http://technorati.com/tag/data+mining`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/feature+space`
[^10]: `http://technorati.com/tag/machine+learning`
[^11]: `http://technorati.com/tag/text+mining`
