# Setting up a Server

_June 26, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/06/setting-up-server.html`

Up until now, all of the hacks that I've posted here have been client-side[^1] and somewhat labor-intensive. If you want to try it yourself (and that, after all, is the point of hacking) then you have to set up Perl on your own computer, download the appropriate files and start modifying them.  

For some time, I've been planning to buy and set up a server, and the recent Doing Digital History workshop[^2] at the Center for History and New Media at GMU gave me the impetus to do so. So I ordered a server, and, in the meantime, have been doing test installations of server software on my home machine, so I have some idea of what to expect. The new server will be a not-very-expensive Windows XP Pro machine with 2Gb of RAM and two 320Gb hard drives. I will be using open source software whenever possible. After three days of installing, testing, making mistakes, uninstalling, and trying again, I've come up with the following sequence.  

1. Install XAMPP[^3]. In order to run a minimal server, you're going to need a webserver (Apache[^4]), a database server (MySQL[^5]), FTP client and server (FileZilla[^6]), a way to make dynamically generated web pages (PHP[^7]) and an all-purpose programming language (Perl[^8]). In my first few attempts, I tried installing these packages separately and then trying to get them to work together. This turned out to be less straightforward than I had hoped, and I was in the process of trying to debug my installation when I discovered that it is possible to install everything you need in one pass. This is not only much faster, but everything works together as advertised. Once the basic XAMPP package is installed, you will want to install the Perl and mod\_perl addons[^9], and fix potential security holes[^10]. Before the following step, you will also need to enable CURL for PHP[^11].  

2. Install WordPress[^12]. At the workshop, I was very impressed with the way that Josh Greenberg[^13] was able to quickly set up a workshop website, blog, syllabus, links to readings, individual blogs for class members, group blog feed and wiki. The magic behind this was WordPress, a popular open source package. If CURL is enabled for PHP (see step 1) it is very easy to import your existing blogs from Blogger and other popular sites. There are also a number of different themes available to change the look and feel of your site or of various parts of it. After playing around with Alex King's Theme Browser[^14], I downloaded about a dozen themes for further experimentation.  

3. Install Streetprint Engine[^15] and/or Greenstone Digital Library Software[^16]. I want our public and digital history students to be able to create online repositories with a minimum of effort. These two packages both worked very well in my test installations; the former is easier to use and more oriented toward page-at-a-time display of images or artifacts, while the latter is oriented more toward libraries. I will probably install both and use whichever is more appropriate to a particular project.  

4. (Optional) Install content management system. I experimented with Joomla![^17] and Drupal[^18] and decided not to install a CMS, at least not yet. Both systems allow users to create database-driven websites without programming, but I figure that WordPress will give me most of the functionality that I need. Besides, I want my students to program!  

More once the server is up and running...  

Tags: blogs[^19] \| digital history[^20] \| hacking[^21] \| open source[^22] \| perl[^23] \| relational databases[^24] \| server[^25]

---

Previous: [A Roundup of Digital History Blogs](20060621-roundup-of-digital-history-blogs.md)  
Next: [Retconning?  Or Revision?](20060628-retconning-or-revision.md)  
[Back to the blog archive](../README.md)

[^1]: `http://en.wikipedia.org/wiki/Client-side`
[^2]: `http://echo.gmu.edu/workshops/june2006/`
[^3]: `http://www.apachefriends.org/en/xampp-windows.html`
[^4]: `http://www.apache.org/`
[^5]: `http://www.mysql.com/`
[^6]: `http://sourceforge.net/projects/filezilla/`
[^7]: `http://www.php.net/`
[^8]: `http://www.perl.org/`
[^9]: `http://www.apachefriends.org/en/xampp-windows.html#1176`
[^10]: `http://www.apachefriends.org/en/xampp-windows.html#1221`
[^11]: `http://www.menyhart.net/blog/developer-stuff/enabling-curl-on-xampp/`
[^12]: `http://wordpress.org/`
[^13]: `http://www.epistemographer.com/`
[^14]: `http://www.alexking.org/software/wordpress/theme_browser.php`
[^15]: `http://www.crcstudio.arts.ualberta.ca/streetprintorg/`
[^16]: `http://www.greenstone.org/cgi-bin/library`
[^17]: `http://www.joomla.org`
[^18]: `http://drupal.org`
[^19]: `http://technorati.com/tag/blogs`
[^20]: `http://technorati.com/tag/digital+history`
[^21]: `http://technorati.com/tag/hacking`
[^22]: `http://technorati.com/tag/open+source`
[^23]: `http://technorati.com/tag/perl`
[^24]: `http://technorati.com/tag/relational+databases`
[^25]: `http://technorati.com/tag/search`
