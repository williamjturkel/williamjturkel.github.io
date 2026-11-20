# Geo-DJ, Part 1: The Idea

_December 3, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/12/geo-dj-part-1-idea.html`

In some of my earlier research on what I called place-based computing[^1], I used handheld and tablet computers with GPS receivers to present archival materials to historians during fieldwork. Say you are standing in front of an old building. The system uses the GPS to determine your location, which is plotted in a geographic information system (GIS). The GIS layers include georeferenced[^2] historical maps and aerial photographs, so you can see what was around your present position (or thought to be around your position) when those historical representations were created. The GIS also includes hyperlinks to other kinds of historical sources, like photographs of buildings and streetscapes, census returns, newspaper articles, city directories, and so on. You can click on a digitized source to consult it, comparing it with the material sources that accumulate naturally in the archive of place[^3]. The system tested pretty well for individual researchers and small walking tours, although our prototypes were not very robust, had relatively short battery lives and could be difficult to read in direct sunlight.  

The system that I am designing now, the ***geo-DJ***, expands this work into an ambient, auditory dimension. Imagine walking around outside with an iPod-like device that is playing an electronic soundtrack. The music changes as you move, reflecting the historical land use patterns of the area that you are exploring. You may choose to represent patches of original forest with a flute, a dairy farm with bass viol and cow bells, a factory with a percussion ensemble, a slaughterhouse with discordant horns. As you walk towards the site of an old factory, the sounds of percussion rise in volume to dominate the music. Like the earlier place-based systems, the geo-DJ includes a GPS receiver and is based on GIS technology. The system determines your present position, then calculates distance and direction from the centroids[^4] of the historical features of interest. That data will then be used to mix the audio tracks that represent each feature.  

At the moment, I'm working with a number of different hardware designs. The easiest ones to build will make use of the same handheld / GPS / GIS platform that I used earlier. I'm also experimenting with using dedicated audio hardware and microcontrollers like Arduino[^5]. Although I envision using the system as a history appliance[^6], many other applications are possible. I'll be posting software and hardware notes here for other people who want to hack the geo-DJ.  

Tags: ambience[^7] \| digital history[^8] \| electronica[^9] \| hacking[^10] \| historical consciousness[^11] \| history appliances[^12] \| place[^13] \| place-based computing[^14]

---

Previous: [Physical Computing Cards](20071120-physical-computing-cards.md)  
Next: [On Blogs and Frogs](20071228-on-blogs-and-frogs.md)  
[Back to the blog archive](../README.md)

[^1]: `http://digitalhistory.uwo.ca/pbc/`
[^2]: `http://www.gsd.harvard.edu/gis/manual/georeferencing/index.htm`
[^3]: `http://www.amazon.com/Archive-Place-Unearthing-Chilcotin-Plateau/dp/0774813768/`
[^4]: `http://www.gsd.harvard.edu/gis/manual/vector/index.htm`
[^5]: `http://www.arduino.cc/`
[^6]: `http://digitalhistoryhacks.blogspot.com/search?q=%22history+appliance%22`
[^7]: `http://technorati.com/tag/ambience`
[^8]: `http://technorati.com/tag/digital+history`
[^9]: `http://technorati.com/tag/electronica`
[^10]: `http://technorati.com/tag/hacking`
[^11]: `http://technorati.com/tag/historical+consciousness`
[^12]: `http://technorati.com/tag/history+appliances`
[^13]: `http://technorati.com/tag/place`
[^14]: `http://technorati.com/tag/place+based+computing`
