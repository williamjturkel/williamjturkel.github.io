# History Appliances: Spöka

_July 19, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/07/history-appliances-spka.html`

On a recent trip to Ikea I came across this awesome little dude[^1]. They're selling Spöka as "children's lighting," but it was pretty clear to me that it was one hack short of a history appliance. It has a rechargeable battery, so that you can use it without it being plugged in. If you slide off the rubber skin, there is a light-bulb-shaped plastic housing inside.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDIq6ZOn4t_igXx_p9d3-MI6Yw-yNYntdWiQmIKhDRgFvls3uq4wVa3zyql5Eo99WrvsqfcIVJcWHRU5WyIriskLhD5d8x40x-IrKHrSU1W3Y5MMGqp4SF2xrWlyrRI9axsdANbA/s200/spoka-001-1024.jpg)  
  
The designer thoughtfully created a case which can be opened into three parts and reassembled with nothing more than a small screwdriver.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoNtYtAgydqSY1Lo-bTPFoH5hOYNgOkFljJCM2WMahWg4raQCUOcxLbwntwBrp0qrl6BE43PRGbIczWbbveh7tf2NQqIDjmUr2Lo44RZ_GAVZhVUOh2TyKxQTEHT8wSouY7zfi6w/s200/spoka-002-1024.jpg)  
  
On the top you'll find a simple push button toggle to turn it on and off.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTqFkqh66xQyvtRrjX2GNzF2ZJNDaQ3Xzr5rP1Yt-IlXwktfY57agkoIyaBHxQz4xStnB3X2HDPaqlMa98wmcW54oT1Cre_MEj-bASnhOhyQdrcURBK2n69LLw30-ksRnY9HKEhw/s200/spoka-003-1024.jpg)  
  
We want to be able to control the light with the computer, however, so I interrupted the power supply by cutting the circuit to the battery and soldering in a pair of wires (the blue ones). I put a bit of heat-shrink tubing over the joints to make them more resilient. I also knotted the wires to provide strain relief where they will emerge from the case.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_3J-pP9ceWw1JCzy-J830K6UJKGLN_vkNa1LffYXkIAp5dcHZwABTzf5ax_acnmkiyYZm-waLzb5KBT3oLLcC0LQjdpS0tVd_U3RwARSIOaiZ4ITjhyphenhyphenTeKooHjAcQ7xGhmepeuQ/s200/spoka-005-1024.jpg)  
  
When the case is reassembled, the wires can be fed out of the top of the hole where the recharging plug goes in.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj38kyN3FJQJwAsg7ZaXcE0CR7iggGXEEsZ_mS5NXjcDrdlOBJxkAASDPhv13dm5QSlXr6HcFCWo14DJAvuNAynmaxHoIZbHC78AgghuB8HkVLq5XHd9Fd3eGSuTPvO96WyyqR7YA/s200/spoka-007-1024.jpg)  
  
After you slide the rubber skin back on, you have an LED-lamp that can be controlled by your computer. If you want to wire it up directly, you might use your parallel port, like Eric Wilhelm does for the haunted house controller[^2] in Make volume 3. Instead, I incorporated it into my standard history appliance rig, which uses Phidgets[^3] controlled by Max/MSP[^4].  
  
For a quick demo project, I created a browser that lets me look through historic newspaper articles about séances from the online Globe and Mail archive. While browsing the stories from a particular time period, Spöka flashes gently in the background, faster if there are a lot of them, slower if not. It provides a nice peripheral feel for the intensity of Spiritualist activity at that point in time.  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPHA2UrLX2EWuJQ2P6tp-i8DLrd9We-WTbYKelx6t3HFWjYAOIERO31Ss0zQHGchIKFiYwLdjn3LlAx9jfvwtuei6Lpt94unyOmRkm-L5Xl0zkIwsCliv-cAFjP8vEcAovaNALaA/s200/spoka-009-1024.jpg)  
  
Tags: ambience[^5] \| hacking[^6] \| history appliances[^7] \| Max/MSP/Jitter[^8] \| phidgets[^9]

[Back to the blog archive](../README.md)

[^1]: `http://www.ikea.com/ca/en/catalog/products/90064441`
[^2]: `http://www.makezine.com/03/halloween/`
[^3]: `http://phidgets.com/`
[^4]: `http://www.cycling74.com/`
[^5]: `http://technorati.com/tag/ambience`
[^6]: `http://technorati.com/tag/hacking`
[^7]: `http://technorati.com/tag/history+appliances`
[^8]: `http://technorati.com/tag/max+msp+jitter`
[^9]: `http://technorati.com/tag/phidgets`
