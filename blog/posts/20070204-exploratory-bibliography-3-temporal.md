# Exploratory Bibliography 3: Temporal Strata in Recommendations

_February 4, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/02/exploratory-bibliography-3-temporal.html`

We've been using the digital history reading list[^1] as the basis for a series of hacks that make use of some of the features of the Amazon API[^2] to explore the conceptual space around a sample bibliography. In the first post in the series, we spidered customer recommendations to find other books[^3] that might be of interest. In the second post, we visualized the network[^4] of recommendations using the freely-available Graphviz package. One of the things that we noticed was that there was a tight cluster of digital humanities 'classics' published between 1991 and 2002, bound together by recommendations but not linked into the larger network. This suggested that we might find temporal strata in recommendations ... that is, that books of a particular era might be linked to one another by customer recommendations, but not linked to books published much earlier or later.  

Today we will explore that hypothesis a bit further. We don't have nearly enough data to make any claims about customer recommendations in general, but this is supposed to be exploratory hacking. We're looking for phenomena that might be of interest, for studies we might want to undertake later on large data sets.  

As every programmer knows, most of the trick to solving a problem algorithmically is to represent the data in a way that makes the answer easy to find. At the conclusion of our last hack, we had a long list of Amazon Standard ID Number (ASIN) pairs representing recommendations: "if you liked that, you'll like this." Now what we need to do is to submit each ASIN to the Amazon API and get the publication date. Then we will have a long list of date pairs: "if you liked that book published in year x, you'll like this book published in year y." We then transform those pairs into a matrix. Some quick-and-dirty Python source to do most of the work is here[^5].  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiokCk0S_dWYW149caKglSkYeLghv-ppNMN_uOhjMFKL4UaHY1WSYtYUGwRPgSzQdvRilwQRn2OQliNpxeEXt9sqT4Q_uCMUWO3B284Zrf_Xx5e8vcJHNhkMO3H9MgIppwiCgavYw/s200/expbib-06.jpg)  

Now, for any given year that books on our list were published, we can see how many recommendations were for books published earlier, how many for books published the same year, and how many for books published later. If you look at the figure above, I've put boxes around the diagonal which represents the case where both books were published the same year. Everything to the left of that boxed cell is a recommendation that was published earlier; everything to the right is a recommendation that was published later.  

Without too much generalization, we can say that it appears that the recommendations for books published earlier tend to be more spread out in time than the ones for those published more recently. This may reflect the fact that those books have had more time to take their place in the literature, or it may be due to the fact that Amazon hasn't been collecting data for very long and has been growing during that time, or to some other factor(s).  

We want to be a bit careful about comparing different rows in the matrix, because most of the books that are on the digital history reading list were published relatively recently (many in 2006). So we can't look at the blob of color in the lower right hand corner, for example, and conclude that most recommendations are to recent books. Instead what we have to do is normalize our data by determining what proportion of recommended books were published earlier, the same year as, and later than a given year. That is shown in the figure below.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqG_dyvqBLYCT_gUCEXsB6NQiGV0Tj-xWoEEGUoiQgPZlcQfG5ucElpixP1b7DxJl7m0xymhqVI6MPBNxx4VopnUAEk2M1Rw8cW6EIzQ1gOsKE4dis971hM55ot4RiX2qtz-Cx-A/s200/expbib-06b.jpg)  

It appears that recommendations for earlier books tend to be to those published later, and recommendations for later books tend to be to those published earlier. And finally, it appears that a growing proportion of recommendations are to books published the same year. The fact that the year 2001 seems to be an exception to this trend may be worth investigating.  

Tags: Amazon[^6] \| application program interface[^7] \| bibliography[^8] \| hacking[^9] \| python[^10] \| visualization[^11]

---

Previous: [More Readings for a Field in Digital History](20070201-more-readings-for-field-in-digital.md)  
Next: [Syllabi for Digital History Classes](20070210-syllabi-for-digital-history-classes.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2007/01/readings-for-field-in-digital-history.html`
[^2]: `http://www.amazon.com/gp/browse.html?node=3435361`
[^3]: `http://digitalhistoryhacks.blogspot.com/2007/01/exploratory-bibliography.html`
[^4]: `http://digitalhistoryhacks.blogspot.com/2007/01/exploratory-bibliography-2.html`
[^5]: `http://digitalhistory.uwo.ca/dhh/hacks/exploratory-bibliography-06.py.html`
[^6]: `http://technorati.com/tag/amazon`
[^7]: `http://technorati.com/tag/application+program+interface`
[^8]: `http://technorati.com/tag/bibliography`
[^9]: `http://technorati.com/tag/hacking`
[^10]: `http://technorati.com/tag/python`
[^11]: `http://technorati.com/tag/visualization`
