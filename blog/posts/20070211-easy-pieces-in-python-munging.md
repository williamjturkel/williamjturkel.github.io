# Easy Pieces in Python: Munging

_February 11, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/02/easy-pieces-in-python-munging.html`

Often you find yourself with a file of data in one format, and you'd really like to have it in a different format. In this situation, writing short, one-off scripts is sometimes known as munging[^1]. It's the kind of thing that Python[^2] is really good for.  
  
Yesterday I posted a list of digital history courses in two formats, as an Excel spreadsheet, and as a CSV (comma separated values) file. The spreadsheet format is proprietary, and more-or-less useless unless you want to manipulate your data in Excel. The CSV file is more promising. It is a simple text file with one data record on each line, the fields separated by commas. But if we had the same data in an RSS[^3] file, it would be even more useful, because we could pop it into a feed reader, or use it for some devious hack in the brand new Yahoo! Pipes[^4].  
  
Besides a header line that we will have to get rid of, the CSV file is flat. That is to say that there is one record per row but no other structure. RSS files consist of nested elements: the whole thing is an RSS block, containing one channel, which has a header followed by a series of items. So when we are building our RSS file, we want to create the header, loop through our CSV records to create the items, then finish with a footer. In fact, munging tasks often have three parts: do something to get ready, process the file(s) a line at a time, do something to finish up.  
  
We start by opening our CSV file and discarding the header line:  
 `datafile = open('digital_history_courses_20070210.csv', 'r')  
datafile.readline()`  
Next we open our RSS file and write the header:  
 `feedfile = open('digital_history_courses_20070210.xml', 'w')  
feedfile.write('<?xml version="1.0"?>\n')  
feedfile.write('<rss version="2.0">\n')  
feedfile.write('\t<channel>\n')  
feedfile.write('\t\t<title>Digital History Courses</title>\n')  
feedfile.write('\t\t<link>http://digitalhistory.uwo.ca/dhh/hacks/digital_history_courses_20070210.csv</link>\n')  
feedfile.write('\t\t<description>Example of munging CSV to RSS 2.0</description>\n')`  
Then we use a loop to parse each line of the CSV file and write a corresponding item for the RSS file:  
 `for line in datafile.readlines():  
    items = line.split(',')  
    school = items[0]  
    course = items[1]  
    if course == '': course = 'N/A'  
    title = items[2]  
    instructor = items[3]  
    year = items[4]  
    url = items[5]  
    feedfile.write('\t\t<item>\n')  
    feedfile.write('\t\t\t<title>' + title + '</title>\n')  
    feedfile.write('\t\t\t<link>'+ url.rstrip('\n') + '</link>\n')  
    feedfile.write('\t\t\t<description>\n')  
    feedfile.write('\t\t\t' + course + ', ' + instructor + ', ')  
    feedfile.write(school + ', ' + year + '\n')  
    feedfile.write('\t\t\t</description>\n')  
    feedfile.write('\t\t</item>\n')`  
Finally, we write the RSS file footer and close our two files:  
 `feedfile.write('\t</channel>\n')  
feedfile.write('</rss>\n')  
datafile.close()  
feedfile.close()`  
That's all there is to it. Most of the hassle is in getting the tabbing and newlines right, and dealing with the odd missing bit of information (in this case, some of the courses don't seem to have numbers.) The RSS file that we created is here[^5]. Now you can easily add it to a feed reader like Bloglines[^6], as shown below.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkk0lvMUxWFRd8M58HfnsWY2DmYftWBXoB52Lmj36ZUqk6TI2AFhHOfjKGd5cr64Yb9Jv4d8EHgoAJBp1nEvWicIp6KHqdFGZjxCpd7ty94dUSGQqhyP1ghLQIqg0nHOXTq7KOvA/s200/rssfeed.jpg)  
  
Tags: hacking[^7] | munging[^8] | Python[^9] | RSS[^10] | XML[^11]

[Back to the blog archive](../README.md)

[^1]: `http://www.science.uva.nl/~mes/jargon/m/munge.html`
[^2]: `http://python.org/`
[^3]: `http://www.xml.com/pub/a/2002/12/18/dive-into-xml.html`
[^4]: `http://pipes.yahoo.com/`
[^5]: `http://digitalhistory.uwo.ca/dhh/hacks/digital_history_courses_20070210.xml`
[^6]: `http://www.bloglines.com/`
[^7]: `http://technorati.com/tag/hacking`
[^8]: `http://technorati.com/tag/munging`
[^9]: `http://technorati.com/tag/Python`
[^10]: `http://technorati.com/tag/rss`
[^11]: `http://technorati.com/tag/xml`
