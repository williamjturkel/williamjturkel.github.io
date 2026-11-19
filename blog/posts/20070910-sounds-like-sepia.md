# Sounds Like Sepia

_September 10, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/09/sounds-like-sepia.html`

One of the things that I was working on over the summer was finding more ambient ways to communicate historical knowledge. As part of that work, I've been recording soundscapes and have gotten in the habit of making a test recording outside my house before setting out. When listening to these test recordings the other day I noticed something odd. I could hear the sound of crickets and other insects, a distant car engine, snatches of music on the breeze, birds, the indistinct voices of children playing. Even though I had recorded the track only a few days earlier, I felt like I could be listening to any summer morning in my lifetime. Somehow the sounds had become unstuck from the time I recorded them and were lazily drifting around. Or so it seemed.  
  
It's hard to investigate a feeling but I decided to give it a little more thought. When we are able to see something that is making noise we readily correlate the sound with the object. This can be disrupted a bit in cases where it takes the sound a noticeable amount of time to reach us, as when watching someone bat a baseball from a distance. We judge the distance of a sound source that we can't see in part by its amplitude--quieter things tend to be farther away--and in part by the environmental coloration that the sound has undergone. A sound that reaches our ears directly arrives there before reflections of that sound off of stuff in the environment. If the reflections arrive quickly, they change the timbre of the perceived sound. If they arrive slowly they are perceived as echoes. The ability to record a sound and play it back later makes it possible to create arbitrary temporal distance between the source of a sound and its perception.  
  
What I got to wondering was whether environmental coloration might be used to make a sound seem as if it were coming from a more distant past. A visual analogy might be coloring a photograph with sepia tones (cheesy[^1]) or filtering the image to simulate the aging of old film (better[^2]). In order to experiment, I set up the following hack.  
  
First, I built a simple circuit to generate a relatively pure tone using the handy 555 timer[^3] and a few other components. I set up a digital audio recorder right above the circuit and recorded a few seconds of irritating buzz. The rig is shown in the photo below... the white thing on the speaker is half of a Nalgene container that I used for a resonator. I've included the schematic in case you want to make your own. You can lower the pitch by increasing the resistance of the 100K resistor and raise it by decreasing the resistance.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKmXL6vd9fsZnYKzT_VISHKVCP0wSgR-2qXpKW4EF7lCtvjIXpAEXpwJATz8-G-oXv4UD482l2_G17slaoGOVlkzoCcRHwN2BShDi_7A2SA24iWWo4Qou5av8wn9B3g7DETa2fiQ/s200/ec-circuit.jpg)  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxbvaoMX_bD_CcpumrADuGVpWRNU8ZfX_oz1maHuoTF94HoXqVIJhwoSsX9OsQtL8c5-jNmygTBkCJwxS_riedhE_tmvKX9NXzSNaKBCAhdiqG_QkQvOHkpsUZIFMeZH5O4Q0rZA/s200/ec-rig.jpg)  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiOk3Jp8tYhV7vn6on9LTmuC0pl7OQSwi0nioKEQQBnfamHb1LguUqg_iYei-2aWZfOygzw0r7sw0AlkMMEgnuI1I9NqpYpdCzrvzlomvgbaRCD1akSKFj_574poJw1R9ezQyoxA/s200/ec-schematic.jpg)  
  
When I recorded the sound of the tone generator right above the circuit it sounded like this[^4] (WAV file). I then moved the recorder to a position about 10 feet away, near an open window. Finally I moved it into another room about 20 feet away. Using Audacity[^5], I amplified both of these recordings so that the overall sound level was the same as the first one (-21 dB). The recording made at an intermediate distance sounded like this[^6] (WAV file) and the one made at the far distance sounded like this[^7] (WAV file). Using the frequency analysis capability of Audacity, it is easy to see the effect of distance and noise on the subsequent recordings.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7M7PpSCppadRh3xVHhdAfv9J8qFdZCJsZaTdV5fEnT8kSLGKW-YRgZvW8KBMJOUQPC0RG6CI33h4e5qgoA4uodnVCfKSPvZROSvL63IpmwBMxjtgPiXQ-71kqoehwMGxBdVcmfA/s200/ec-freq-analysis.jpg)  
  
Does environmental coloration make the sound seem more distant in time as well as space? I'm not sure. I thought I'd put it out there in case anyone else has the same perception, or wants to hack the hack.  
  
Tags: ambience[^8] \| digital history[^9] \| hacking[^10] \| soundscapes[^11]

[Back to the blog archive](../README.md)

[^1]: `http://www.niksoftware.com/colorefexpro/usa/entry.php?info=colorefexpro/samples//midsepia.shtml`
[^2]: `http://www.niksoftware.com/colorefexpro/usa/entry.php?info=colorefexpro/samples//opc.shtml`
[^3]: `http://www.uoguelph.ca/~antoon/gadgets/555/555.html`
[^4]: `https://sites.google.com/site/digitalhistoryhacks/Home/data-files/ec-close.wav`
[^5]: `http://audacity.sourceforge.net/`
[^6]: `https://sites.google.com/site/digitalhistoryhacks/Home/data-files/ec-med.wav`
[^7]: `https://sites.google.com/site/digitalhistoryhacks/Home/data-files/ec-far.wav`
[^8]: `http://technorati.com/tag/ambience`
[^9]: `http://technorati.com/tag/digital+history`
[^10]: `http://technorati.com/tag/hacking`
[^11]: `http://technorati.com/tag/soundscapes`
