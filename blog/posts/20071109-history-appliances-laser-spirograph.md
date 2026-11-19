# History Appliances: Laser Spirograph

_November 9, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/11/history-appliances-laser-spirograph.html`

A sure sign of a 1970s childhood is a fond memory of doodling with the Kenner Spirograph[^1] toy. In the back of my mind I've been thinking it would be fun to build something like it into a history appliance. You can already find software versions[^2] online, but I wanted something that could be used at the periphery, rather than the focus, of attention. On a recent trip to Active Surplus[^3] in Toronto I realized I could build a version quite cheaply. So here it is: a little too thrown together even to call a hack, this is really a kludge[^4].  
  
I started by cutting a $1 laser pointer out of its casing and soldering some wires to it so I could switch it on and off electronically. Here it is on a breadboard with a 5v voltage regulator.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXatzW6yCi3xz2mjaDJukgsURqV_I1zbizUmFXGx-s8AjF-_DNbagmFRRHzVK-CwrGP_ZicdBuf0rONNFNJe4lnvAC5AT1HN95042byq8ZyTvQF-xnvyv1-4nSXK_IYIiGV-OJIA/s200/Laser-Spirograph-laser.jpg)  
  
The laser shines on a mirror that is crazy-glued to a cylindrical piece of dense foam and mounted on the shaft of a motor. I used Lego motors because I had a pair of them. The reflection bounces off another mirror, similarly mounted, and is projected on to a screen made from a 3x5 card. The motors tend to slip around when they are running so I put a rubber mat under each.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtFXJdFP_j3hpWqVDTyFkOayCT7lhEswY3Pb3kwp82k4eramD7legB7wR-F8OiZFyTGQvSoyxDRcMiWzUuaV8WwKVyDbDOdu2ExsyOrXVWnA2iWU96IdAq2fJYLUJLwpBUTDOV1w/s200/Laser-Spirograph-motors.jpg)  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAd7VFOLvCeoJCKzP9rR5v6cuoN08D_VAQfKog1cNsaTGeJysu_zKdJ40xTCYBpy46Zqgzgzuapr4LVepFEoB9-k5I2jZwC71T_VgnvmHHXhtZ6BFtKIJORDc9-KbJnRNBPX0NpA/s200/Laser-Spirograph-screen.jpg)  
  
The motors are controlled by pulse width modulation, using a Phidgets MotorControl LV[^5] board. I used a wall wart to supply 9v for the motors.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0iwnxCk9dJz159OuQWUaJAX-euBzxrc_SusbAuhD1pv_BeG1wXW0iRAlM6UuCGuYofb3-2gvcqoHlODyYm7Zhs0nat3KxBZTlyc2Y_awECLjfW6SUj0f5anovh8ak6Ep5hyflVw/s200/Laser-Spirograph-motorcontrol.jpg)  
  
To be able to fiddle with the speed of each motor, I used the Phidgets Interface Kit[^6], the mini joystick[^7] and a Max/MSP[^8] patch.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCvdsVnnooUB48TgIFM3EAYXKnu_Y9cROEoejxVbJH7FQ7xqZk7-iwOT4o_DFtYdxiWVfbGFFotkdNHQkSWIEFRA96PQkc7SHMPVuLbn9KrGp_Nz-xIKrhMhs2yFFqdGYKiiGU2w/s200/Laser-Spirograph-interfacekit.jpg)  
  
The whole setup looked like this.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWkZItAwpZ-O0znM8AqPnfB2cBd6iqzqu_mWg4xrm_3znCVpWpPOriVFfgrGjLfqp3wy5lPxSbE-eYEoYqATT_IIaIE1WFVStBzL3pR292zo-hMeyMcvPZOSp6ykKDPo2p6Sdb8A/s200/Laser-Spirograph-setup.jpg)  
  
With the motors both running, the dot of the laser pointer is perturbed by first one rotation, then the next, tracing out a familiar spirograph-style image.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHn2TJ0uRZESRLoitLKv8t0qN2Qwrygx33Spl3PIr8lsnigaLQX26AadNLHa5K9L3vXDLVpp6iHAP_4KpL4urQZd0GJjSE47-UqPnBYcHhPwOIXXJjwqPmBUBvP9plptEpr9FKxA/s200/Laser-Spirograph-big.jpg)  
  
As you vary the speed and direction of rotation for the two mirrors, you get a range of different patterns.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfzixNX6tj6V6PXgokzWxlqbdZ_Fwhtl-SpzZWAWw6XhId9A2Ev0LHREyBxRuOsI6aKT96Dj-qTQV9xImq3rKWcjajrr30S25ao76fQR5IdlvttGjQHgiwpGn6bxjmaO8smUTKZw/s200/Laser-Spirograph-collected.jpg)  
  
To demonstrate, I used the joystick to vary the parameters of the system. In an application, it would be hooked up to streaming data instead. Groovy!  
  
Tags: ambience[^9] \| hacking[^10] \| history appliances[^11] \| nostalgia[^12]

[Back to the blog archive](../README.md)

[^1]: `http://www.journalofantiques.com/Jan07/playing_around.html`
[^2]: `http://www.math.psu.edu/dlittle/java/parametricequations/spirograph/SpiroGraph1.0/index.html`
[^3]: `http://www.activesurplus.com/`
[^4]: `http://catb.org/jargon/html/K/kluge.html`
[^5]: `http://www.phidgets.com/products.php?product_id=1060`
[^6]: `http://www.phidgets.com/products.php?product_id=1018`
[^7]: `http://www.phidgets.com/products.php?product_id=1113`
[^8]: `http://cycling74.com/products/maxmsp`
[^9]: `http://technorati.com/tag/ambience`
[^10]: `http://technorati.com/tag/hacking`
[^11]: `http://technorati.com/tag/history+appliances`
[^12]: `http://technorati.com/tag/nostalgia`
