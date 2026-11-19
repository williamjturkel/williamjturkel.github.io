# Microsoft Live Labs Photosynth and Place-Based Computing

_August 2, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/microsoft-live-labs-photosynth-and.html`

One of my research programs is in what I call place-based computing[^1]. By combining digital sources with geographic information software (GIS), global positioning receivers (GPS) and handheld or tablet computers, it becomes possible to access historical sources in the place that the source represents. You can stand outside of an old building, for example, and see photographs of how it used to look, census or ownership records, old newspaper articles about it, and so on. We introduced the technology in the Western Public History MA program[^2] last year, when our grad students used it to create a technology-enhanced walking tour of a heritage conservation district.  
  
Up until now, most of the sources that we've been using for place-based computing have been geocoded by hand. If we know that a newspaper article refers to a particular building or intersection, we can use a web service like Geocoder.ca[^3] to determine the latitude and longitude, and then make an entry for the source in the GIS database. Part of the impetus for text and data mining is to automate this process. (One might, for example, use web services to geocode every place name in the Dictionary of Canadian Biography, then download the entire thing to a handheld. Then when you visited Chicoutimi, you could discover that Dominique Racine[^4] was parish priest there from 1862-88, that William Price[^5] and Peter McLeod[^6] had timber operations there in the 1840s, and so on. In effect, the system would be a travel guide that emphasized Canadian historical biography.)  
  
Techniques for mining text are relatively well-understood compared with those for mining images. At this point, a number of Canadian archives, such as the McCord Museum[^7] and the BC Archives[^8], have large repositories of digital historical images. Many of these are images of places, although the metadata does not include tags for latitude and longitude. Ideally, it would be possible to sift through these images automatically, returning ones that matched, say, a present-day photograph of an existing structure.  
  
As a preliminary step in this direction, I got a small grant to experiment with using some off-the-shelf photogrammetry software (PhotoModeler[^9]). I used photographs of a present-day building to create a partial 3D model, then imported historical photographs of an adjacent building that had been demolished. The software allowed historical and contemporary photographs to be displayed in the same 3D space, although the work is painstaking, to say the least. (You can read the report here[^10].)  
  
Enter Photosynth[^11], from Microsoft Live Labs. Researchers recently announced a pretty amazing new tool that automatically extracts features from images, uses photogrammetry to stitch them together in three dimensions and then gives you an immersive browser to explore the whole thing. Their demo shows the system with contemporary photographs, but historical photographs should work as well. I can't wait for a chance to play with their software.  
  
Tags: GIS[^12] \| GPS[^13] \| historical photographs[^14] \| immersive environments[^15] \| photogrammetry[^16] \| photosynth[^17] \| place-based computing[^18] \| text mining[^19] \| visualization[^20]

[Back to the blog archive](../README.md)

[^1]: `http://digitalhistory.uwo.ca/pbc/`
[^2]: `http://history.uwo.ca/gradstudy/publichistory/`
[^3]: `http://geocoder.ca`
[^4]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=39906`
[^5]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=38781`
[^6]: `http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=38204`
[^7]: `http://www.mccord-museum.qc.ca/en/`
[^8]: `http://www.bcarchives.gov.bc.ca/visual/visual.htm`
[^9]: `http://www.photomodeler.com/`
[^10]: `http://digitalhistory.uwo.ca/pbc/index.php/photogrammetry-and-superposition/`
[^11]: `http://labs.live.com/photosynth/`
[^12]: `http://technorati.com/tag/GIS`
[^13]: `http://technorati.com/tag/GPS`
[^14]: `http://technorati.com/tag/historical+photographs`
[^15]: `http://technorati.com/tag/immersive+environments`
[^16]: `http://technorati.com/tag/photogrammetry`
[^17]: `http://technorati.com/tag/photosynth`
[^18]: `http://technorati.com/tag/place+based+computing`
[^19]: `http://technorati.com/tag/text+mining`
[^20]: `http://technorati.com/tag/visualization`
