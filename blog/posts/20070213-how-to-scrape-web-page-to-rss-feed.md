# How To: Scrape a Web Page to RSS Feed

_February 13, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/02/how-to-scrape-web-page-to-rss-feed.html`

{% raw %}
One thing that I've been arguing since I began this blog is that it is essential for historians to learn how to search, spider and scrape[^1] in order to make the best use of online sources. These tasks are relatively easy if you already know how to program. Many historians, of course, don't. I have a semi-regular series on "Easy Pieces in Python[^2]," but I know that at least some of my readers think that I'm stretching the truth a bit with 'easy.' I've decided to start another semi-regular "How To" series for hacks that you can do without any programming at all.  

I regularly read Tara Calashain's wonderful blog ResearchBuzz[^3], so when David Davisson recommended[^4] her new book Information Trapping[^5], I went right out and bought it. It's definitely worth reading ... in fact, I'm thinking of assigning it to my digital history students next year. Without giving away too much of the book, I think it's fair to say that it might have been subtitled "How to do things with RSS feeds." Which is great if you've got feeds. What do you do if not?  

Here's an example. Tables of contents for back issues of the journal Environmental History are stored in an HTML table on a web page[^6] at the Forest History Society. Suppose you want to look through them. You could always go to the page and browse. If you do this every few months, you will see that another issue has been added as a new one is released. Calishain discusses the use of page monitors to track these kinds of changes, so that you don't have to try to remember to visit the site on a regular basis.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid1Vvu4xrQCQe2LnHz_UjNghz9SB6Q7IVzLIIj_1X8sQa1vTHgq3bwfjUQObb8YcqTkjoHl-d1JCeBLLgkJRpDsfmIJ3sVAenFvz-43KufRMGqkbdHgjw1EOtWo69GsqZHbIaH_w/s200/howto01a.jpg)  

Another strategy is scrape the information off of the webpage, transform it into an RSS feed, and make it available where you are going to be spending an increasing amount of your time (i.e., in your feed reader). You can do this without programming by making use of a sweet new free service called Feed43[^7]. Go to the website and choose "Create Your Own Feed." The first thing that it is going to ask you is for an address. Here you enter the URL of the page that you want to scrape:  

```
http://www.foresthistory.org/Publications/EH/ehback.html
```

When you click the button it will load the HTML of the page into a window. Now you need to identify the information you will be scraping from the page. In this case you're going to want the month, volume and issue number, and URL for the page with the table of contents. When you look through the HTML source, you see that an individual entry typically looks like this:  

```html
<font face="Times New Roman, Times, serif"><a href="http://www.foresthistory.org/Publications/EH/ehjan2006.html">January
2006</a> (11:1) </font>
```

Notice that I've included some of the HTML code that surrounds each entry. This is very important for scraping, because the scraper needs to identify what constitutes an entry on the basis of the surrounding code. You want to choose as much surrounding code as you need to uniquely identify the data you're interested in. Once you have identified your data and the surrounding context, you turn it into a pattern by using '{%}' to match data regions as shown below:  

```html
<font face="Times New Roman, Times, serif"><a href="{%}">{%}</a>{%}</font>
```

Enter the above into the "Item (repeatable) Search Pattern," and press the "Extract" button. If all went as planned, the scraper should be able to pull out exactly the information that you are interested in. Your clipped data should look like this:  

```
Item 1
{%1} = http://www.foresthistory.org/Publications/EH/ehjan2006.html
{%2} = January 2006
{%3} = (11:1)
Item 2
{%1} = http://www.foresthistory.org/Publications/EH/ehapr2006.html
{%2} = April 2006
{%3} = (11:2)
```

Note that the three {%} patterns above matched the URL, month, and volume and issue number. At this point we have to define the output format for our feed. We can keep the suggested defaults for the feed properties, but we have to set up patterns for our output items. Set the "Item Title Template" to  

```
{%2} {%3}
```

the "Item Link Template" to  

```
{%1}
```

and since we don't have any content, just set that to a non-breaking space. Click "Preview" to make sure that your feed looks OK. At this point you can subscribe to your feed.  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUa4ue48Ex-3_5TTaCaHXndy4wlUi30kEtcc1WN-K73FXbIBKLZHblDuO1g5Pvx3GbZO9MFwezy-imDU9DL6MagW1VRdzGeLdtOiFoupDW3fY_Xru1nH__S88ynjQmX8jfY7k4rQ/s200/howto01b.jpg)  

Tags: digital history[^8] \| scraping[^9] \| RSS[^10]
{% endraw %}

---

Previous: [Easy Pieces in Python: Munging](20070211-easy-pieces-in-python-munging.md)  
Next: [How To: See the Field at a Glance](20070216-how-to-see-field-at-glance.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2005/12/teaching-young-historians-to-search.html`
[^2]: `http://search.blogger.com/?as_q=%22easy+pieces%22&ie=UTF-8&ui=blg&bl_url=digitalhistoryhacks.blogspot.com&x=0&y=0`
[^3]: `http://www.researchbuzz.org/wp/`
[^4]: `http://patahistory.blogspot.com/2007/01/information-trapping_23.html`
[^5]: `http://www.amazon.com/Information-Trapping-Real-Time-Research-Web/dp/0321491718/`
[^6]: `http://www.foresthistory.org/Publications/EH/ehback.html`
[^7]: `http://www.feed43.com/`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/scraping`
[^10]: `http://technorati.com/tag/rss`
