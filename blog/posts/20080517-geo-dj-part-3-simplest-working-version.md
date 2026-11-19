# Geo-DJ, Part 3: The Simplest Working Version

_May 17, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/05/geo-dj-part-3-simplest-working-version.html`

Some people may have the ability to come up with something awesome on their first pass--say, Athena springing from the forehead of Zeus fully formed--but I've learned that I have to make some mistakes along the way. So I try to come up with the simplest working version of a project, then complexify it gradually. Of course, things being what they are, you can usually improve something by simplifying it, so the first, apparently simplest, version is actually somewhere in the middle[^1] of the scale from perfect to perfectly foobar.  
  
With the geo-DJ, I imagine the simplest working version to be something like a metal detector for historical landscape features. Suppose you know that there used to be an electric streetcar running through the middle of downtown, but most material traces of it have since been torn up. If you have a map of the streetcar route, you can use existing landmarks to georeference it, and determine the latitude and longitude of the endpoints (and any additional inflection points, but let's ignore those and work with a purely linear feature). The locations of the endpoints need to be stored in memory.  
  
As the user walks around, the geo-DJ loops through the following algorithm. First, determine the user's current position. Then, determine the line through the endpoints (the former rail), determine the length of the perpendicular line from the user to the rail line (i.e., the magnitude of a normal vector), and scale the pitch of a tone that is playing in the headphones. Repeat, ad infinitum... or until the batteries drain, whichever comes first. If the user steps toward the rail, the pitch of the sound increases. If he or she steps away from it, the pitch decreases. Using this version of the system, a person can explore the lineaments of landscape features which may no longer exist. See Michal Migurski's great air photo[^2] of San Francisco "healing" around a former railroad.  
  
Tags: ambience[^3] | digital history[^4] | electronica[^5] | hacking[^6] | historical consciousness[^7] | history appliances[^8] | place[^9] | place-based computing[^10]

[Back to the blog archive](../README.md)

[^1]: `http://digitalhistoryhacks.blogspot.com/2008/05/beginning-in-middle.html`
[^2]: `http://mike.teczno.com/notes/scar-tissue.html`
[^3]: `http://technorati.com/tag/ambience`
[^4]: `http://technorati.com/tag/digital+history`
[^5]: `http://technorati.com/tag/electronica`
[^6]: `http://technorati.com/tag/hacking`
[^7]: `http://technorati.com/tag/historical+consciousness`
[^8]: `http://technorati.com/tag/history+appliances`
[^9]: `http://technorati.com/tag/place`
[^10]: `http://technorati.com/tag/place+based+computing`
