# Phidgets: Introduction

_March 18, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/03/phidgets-introduction.html`

Around 2001, University of Calgary computer scientists Saul Greenberg[^1] and his student Chester Fitchett found that their efforts to create new interactive media spaces were impeded by a "quagmire of tediousness." Rather than spending their time designing the kinds of interactions that they were interested in, they had to focus on the disparate elements that made up their demonstrations, things like electrical circuits, components, low-level programming, wiring, and so on. Graphical user interfaces already had software components called "widgets[^2]." These are reusable elements like windows, radio buttons, pull-down menus and check boxes. Once one person has figured out how to implement a widget, other people can add that widget to their interface with much less effort. Wouldn't it be great, Greenberg and Fitchett asked[^3], if there were such a thing as physical widgets? Thus phidgets[^4] were born.  
  
You can now buy reusable physical components to measure light, sound, temperature, pH, vibration, force, human touch and motion and a host of other things in the real world. You can drive servo motors and interact with radio frequency ID chips (RFIDs[^5]). There are two- and three-axis accelerometers (the same kind of device used in the remote of the new Nintendo Wii[^6]). These phidgets are easily combined and recombined because, in the words of Greenberg and Fitchett, "they hide implementation and construction details while exposing functionality through a well-defined API." In other words, you don't have to know how the magnetic sensor works at a physical or electrical level, you just need to know that if you plug it in, it will return a value that represents the strength of nearby magnetic fields.  
  
I've recently gotten a large collection of phidgets to use for both research (more about that later) and for public and digital history student projects. Eventually our students will be able to design and implement things like interactive exhibits and history appliances[^7]. In the meantime, however, I have to make sure that I know how they work and that the lower-level scaffolding is in place. Phidgets don't come with Python[^8] support right now, so I've had to use ctypes[^9] to dig into the dynamically linked C libraries. I know I'm not the only pythonista who wants to hack phidgets right now, so for the benefit of others, here are some partially implemented wrappers for the 8/8/8 interface kit[^10] and the servo 4-motor kit[^11]. Comments and improvements are always welcome, of course.  
  
Tags: hacking[^12] | interaction design[^13] | phidgets[^14] | python[^15]

[Back to the blog archive](../README.md)

[^1]: `http://pages.cpsc.ucalgary.ca/~saul/wiki/pmwiki.php`
[^2]: `http://en.wikipedia.org/wiki/Widget_%28computing%29`
[^3]: `http://grouplab.cpsc.ucalgary.ca/papers/2001/01-Phidgets.CHIWorkshop/phidgets.report2001-681-04.pdf`
[^4]: `http://www.phidgets.com/`
[^5]: `http://www.rfidjournal.com/faq`
[^6]: `http://us.wii.com/`
[^7]: `http://digitalhistoryhacks.blogspot.com/2007/03/coming-soon-history-appliances.html`
[^8]: `http://www.python.org`
[^9]: `http://docs.python.org/lib/module-ctypes.html`
[^10]: `http://digitalhistory.uwo.ca/dhh/hacks/phidgets-interface-kit-demo.py.html`
[^11]: `http://digitalhistory.uwo.ca/dhh/hacks/phidgets-quad-servo-demo.py.html`
[^12]: `http://technorati.com/tag/hacking`
[^13]: `http://technorati.com/tag/interaction+design`
[^14]: `http://technorati.com/tag/phidgets`
[^15]: `http://technorati.com/tag/python`
