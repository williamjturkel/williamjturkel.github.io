# Design for a Kiosk in a Cabinet

_March 6, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/03/design-for-kiosk-in-cabinet.html`

Last year the Western Social Science building was renovated to include shallow glass-fronted display cabinets for each department. A small group of my colleagues gathered in front of ours to discuss how best to portray the department to students and visitors. Some thought that using the cabinet to display a collection of faculty-authored monographs would be boring ... which is funny, because writing such monographs is crucial for promotion and tenure in our department. Anyway, the general consensus was that it would be nice to have something fun, something animated, maybe even interactive.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9G06AhZbUJqH8WmFcrmEzV66LWKrr2D2BRGn80p1TF61KyBOk4vL5aBIMx6OwGkuTZIEdg7QycOn6uVw2BWI4ynjv9GbCotcn7JXpduabwL5cfoAFGYJer_HeFsBQILAnQzLlvA/s200/cabinet.jpg)  
  
The cabinet poses two main design constraints. The first is that it is shallow, so there is room to fit a tablet computer, but not a laptop or desktop. It would also be difficult to fit in an LCD projector unless you wanted to do something catoptric[^1]. The second constraint is that there is an air gap between the user and the display. So they can't touch anything, unlike a regular kiosk. Interactions have to be mediated by photons, or radio waves, or sound. The cabinet is in a busy hallway near people's offices, so sound could get really irritating.  
  
I recently read Analog In, Digital Out[^2] by the interaction designer Brendan Dawes. He's a big fan of using webcams in his designs, and I got to thinking that a camera would be one way to bridge the gap. It would also mean that the user's own image has to become part of the design, but we can use that. Since this will be a public history project, one idea that we might try to convey is situating the user in the flow of time. By themselves, glass display cases superimpose a ghostly image of the viewer onto the contents of the case, so we will really be doubling this effect. (For more on display cases, see Martin Roberts, "Mutations of the Spectacle: Vitrines, Arcades, Mannequins," French Cultural Studies 2 (1991): 211-249.)  
  
I also like the idea of working with flows, something I've been thinking a lot about lately, whether in the form of RSS feeds[^3], perceptual experiences of place[^4], or lines of flight[^5]. So we're aiming for a kiosk design that incorporates the user's image, uses a webcam for interaction, and conveys historical flow in some way.  
  
Here's what I came up with. In the cabinet there's a tablet computer with a webcam facing the user. A series of historical images flows past in chronological order, partially transparent and projected over the user's image. When they reach up to "touch" one of the images, the flow stops and that image is displayed in detail. They're not really touching anything, of course. The camera detects the motion of their hand in the air, and they see themselves touching something on the screen. Here are some screen shots from my demo:  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS5qGi0TLUiPbzzlyVFYCGp_EadaUDFi5KES3ixIBt9VO48E4I06LbmQebpv1hObid2R5RRZINlXw4OgqYMBUnDwqn9zlpmye80FMPpbjDNcgfnpC92BaHgGICDLNCWWr04Yguuw/s200/kiosk01.jpg)  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7PZFDM-qfIX1CiqD2eV8doAr8d5ywuQ8s9ENvnC8CguL9OUM30BkPE1V9BDnQEtBOjJaVqQBed-CnYUYnkJBbfcZpCJSYHzGk2khAAl_5OdSSs8AICQRRPJuX1MCgyV_3aUOq9w/s200/kiosk02.jpg)  
  
You can download the Python source here[^6]. For my demo I used a lovely series of lantern slides from the McCord Museum[^7]. Although the webcam motion detector interface works, I didn't implement the flow part because in an actual installation I would want to use the wireless capabilities of the tablet to tap into an RSS feed of images. That would require a little more programming.  
  
About this post. A couple of months ago I was tagged with a meme and passed it on to Brett Holman[^8], among others, who responded by tagging me with a different meme: the Thinking Blogger[^9] award. Under the original terms of the award, I'm supposed to nominate five blogs which make me think. Instead, I decided to use five blog posts / webpages to inspire a design and teach myself how to do something new.  

1. My former digital history student and all-around humble guy Jeremy Sandor suggested that public history should be play[^10].
2. Brendan Dawes showed me how to use Play-Doh as an interface[^11].
3. Guyon Moree put the pieces together in Python[^12].
4. Paula Petrik[^13] and Jeremy Boggs[^14] continue to emphasize the role of design in digital history.
5. And the ThirdView Rephotographs[^15] suggest a future direction for designs like this one.

You're it!  
  
Tags: flows[^16] \| hacking[^17] \| historical photographs[^18] \| interaction design[^19] \| public history[^20] \| Python[^21] \| webcams[^22]

[Back to the blog archive](../README.md)

[^1]: `http://www.kirchersociety.org/blog/?p=251`
[^2]: `http://www.amazon.com/Analog-Digital-Out-Brendan-Interaction/dp/0321429168/`
[^3]: `http://www.amazon.com/Information-Trapping-Real-Time-Research-Web/dp/0321491718/`
[^4]: `http://www.amazon.com/Ecological-Approach-Visual-Perception/dp/0395270499/`
[^5]: `http://www.amazon.com/Thousand-Plateaus-Capitalism-Schizophrenia/dp/0816614024/`
[^6]: `http://digitalhistory.uwo.ca/dhh/hacks/kiosk.py.html`
[^7]: `http://www.mccord-museum.qc.ca/en/keys/virtualexhibits/magiclantern/`
[^8]: `http://airminded.org/2007/02/20/good-memes/`
[^9]: `http://ilkeryoldas.blogspot.com/2007/02/thinking-blogger-awards_11.html`
[^10]: `http://jeremysandor.blogspot.com/2007/02/play.html`
[^11]: `http://www.brendandawes.com/mt/archives/000162.html`
[^12]: `http://gumuz.looze.net/wordpress/index.php/archives/2005/06/06/python-webcam-fun-motion-detection/`
[^13]: `http://www.archiva.net/hist697ay07/index.html`
[^14]: `http://clioweb.org/archive/2007/01/31/readings-in-design-for-digital-humanities/`
[^15]: `http://thirdview.org/3v/rephotos/index.html`
[^16]: `http://technorati.com/tag/flows`
[^17]: `http://technorati.com/tag/hacking`
[^18]: `http://technorati.com/tag/historical+photographs`
[^19]: `http://technorati.com/tag/interaction+design`
[^20]: `http://technorati.com/tag/public+history`
[^21]: `http://technorati.com/tag/Python`
[^22]: `http://technorati.com/tag/webcams`
