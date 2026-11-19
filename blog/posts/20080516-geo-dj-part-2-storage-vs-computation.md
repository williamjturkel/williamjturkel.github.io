# Geo-DJ, Part 2: Storage vs. Computation

_May 16, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/05/geo-dj-part-2-storage-vs-computation.html`

In my last post, I mentioned that I'm working with a couple of talented students this summer on digital history projects, and talked a bit about Adam Crymble's Zotero translators. The other person who is working with me is Devon Elliott[^1]. Last year Devon came up with a plan to use wikis in archives[^2] and built a model of Sputnik that contained a microcontroller, a thermistor to sense temperature changes and an accelerometer to respond to motion. The information about the model's state was conveyed by modulating the frequency and duration of a beeping signal. Devon did the programming and electronics without any help from me, so I knew he would be the perfect collaborator for the geo-DJ project.  
  
The geo-DJ[^3] is a wearable iPod-like device. As you wander around a present-day environment, it uses GPS to determine your position and synthesizes an electronic soundtrack that reflects former land-use patterns. Creating something like this wouldn't be too difficult using a lightweight laptop or a powerful handheld computer running GIS software. But we're interested in doing the project at as low a level as possible, preferably using an open source microcontroller board like Arduino[^4].  
  
In the history of computing, people often faced the limits of both memory capacity and processing speeds. Consider the problem of determining trigonometric functions for particular values. There are algorithms for computing the sine[^5] of an angle, but they're complicated. Before the widespread adoption of digital calculators it was common for people to use trig tables, a clear case of using more storage space to simplify or speed up calculation. With digital calculators or general-purpose computers, it is simpler and faster to punch in the calculation than to look it up in a trig table. But here is the tricky part: it may not be simpler for the computer to do the computation. The software may involve looking up the value of various trig functions in tables, even though that is not apparent to the user.  
  
Doing the geo-DJ project on a small computer like Arduino approaches these limits in (at least) two places: GIS and music synthesis. In the case of the GIS, we want to know the person's distance from the various points, lines and polygons that are used to represent historical features of interest. There are algorithms[^6] for computing these measures, but our processor is slow and our application requires real-time feedback. It might make more sense to pre-compute the measures and store the information about distances in a multi-dimensional array. Of course, the basic amount of memory on an Arduino is also very limited, so we have to find the optimal balance. In the case of music synthesis, a similar problem arises. Sounds have complicated waveforms which can be computed or looked up in a wave table. Once again, we will have to find the right balance between storage and computation.  
  
It may be that the platform that we're trying to use is too simple. We may have to add more memory, or dedicated signal processing hardware, or both. But that is one of the things that makes a project like this fun. By working close to computational limits we not only have more of a challenge, but more of a sense what computing used to be like, long ago, when we were kids.  
  
Tags: ambience[^7] | digital history[^8] | electronica[^9] | hacking[^10] | historical consciousness[^11] | history appliances[^12] | place[^13] | place-based computing[^14]

[Back to the blog archive](../README.md)

[^1]: `http://devonelliott.blogspot.com/`
[^2]: `http://devonelliott.blogspot.com/2007/10/wikiarchives.html`
[^3]: `http://digitalhistoryhacks.blogspot.com/2007/12/geo-dj-part-1-idea.html`
[^4]: `http://www.arduino.cc/`
[^5]: `http://mathworld.wolfram.com/Sine.html`
[^6]: `http://www.geog.ubc.ca/courses/klink/gis.notes/ncgia/toc.html`
[^7]: `http://technorati.com/tag/ambience`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/electronica`
[^10]: `http://technorati.com/tag/hacking`
[^11]: `http://technorati.com/tag/historical+consciousness`
[^12]: `http://technorati.com/tag/history+appliances`
[^13]: `http://technorati.com/tag/place`
[^14]: `http://technorati.com/tag/place+based+computing`
