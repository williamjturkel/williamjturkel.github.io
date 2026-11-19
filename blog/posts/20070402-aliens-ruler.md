# The Alien's Ruler

_April 2, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/04/aliens-ruler.html`

Back in the days of Usenet, there was a thread[^1] on rec.puzzles about an alien who comes to Earth, encodes the contents of the Encyclopedia Britannica as a single mark on a metal rod and takes it back to his home planet. The gist of the puzzle was that (1) it's possible to encode information as numbers, and (2) if you concatenate a bunch of numbers together and precede them with a zero and a decimal point, you have the decimal representation of a fraction. Assuming the alien knows the length of the metal rod, each possible mark on it would correspond to some fraction.  
  
You probably remember learning that if you're given two different fractions, it's always possible to find another that lies between them. Between three-fifths and four-fifths, for example, is seven-tenths ... not to mention an infinite number of close friends. So what prevents alien or human technologists from using metal rods as arbitrarily dense analog storage devices? Measurement.  
  
Seth Lloyd works through the physics in his enjoyable book Programming the Universe[^2] (pp.22-24):  
> just as there are an infinite number of real numbers between 0 and 1, there are apparently an infinite number of possible lengths between zero meters and one meter. The reason that apparently continuous quantities such as the length of a metal rod can register only a finite amount of information is that these quantities are typically defined only to a finite level of precision. To see the trade-off between precision and information, think of measuring the length of that rod using a meterstick. The meterstick is made of wood. One hundred centimeters are marked and numbered on the stick. One thousand millimeters are marked, ten for each centimeter, but there is not enough room on the meterstick to number them legibly. You can use the meterstick to measure the length of the rod to the accuracy of about a millimeter. Below a millimeter, a meterstick does not measure distances well, simply because its physical characteristics give it a finite resolution. The total number of alternatives is 1,000, corresponding to three digits of accuracy, or about ten bits of information.

  
  
(Think of a bit as a switch that can take two values, 0 and 1. If you have two bits, you can store four alternatives: 00, 01, 10, 11. If you have three bits you can store eight alternatives: 000, 001, 010, 011, 100, 101, 110, 111. With n bits, you can store 2^n alternatives. Since 2^9=512 and 2^10=1024, you need about ten bits to store 1,000 alternatives.)  
  
Presumably aliens have better technology than wooden metersticks. But Lloyd works through a series of measurement devices, showing that each one doesn't buy that much more capability. With an optical microscope or an interferometer you might get six digits of accuracy (about 20 bits). With an atomic force microscope you might get ten digits of accuracy (33 bits)... but that requires the ability to sense individual atoms in the metal rod.  
> To get thirty-three bits of information about the length of our rod, we have to count that length in atoms: heroic amounts of effort are typically required to wring more than a few tens of bits of information out of a single continuous quantity such as the length of a rod. By contrast, if we use many individual quantities to register information, we can rapidly accumulate many bits. ... Our rod contains something like a billion billion billion atoms. If each one registers a bit, then the atoms in the rod can register a billion billion billion bits, far more than the length of the rod on its own can register. In general, the best way to get more information is not to increase the precision of measurements on a continuous quantity, but rather to put together measurements on more and more quantities, each of which may register only a few bits. This compiling of bits--or digital representation--is effective because the number of total alternatives described grows much faster than does the number of bits.

  
  
I bring up this thought experiment because I think it highlights what is interesting about digital history. Digital history isn't just about historical sources stored and manipulated on computers. That's pretty old hat, dating at least to Father Busa's work[^3] with automated concordancing in the 1940s. And digital history isn't just about historical sources represented in digital form, which dates back millennia[^4]. Instead the "digital" of digital history points us toward sites where the digital or analog representation of past events--or the conversion from one form to the other--plays a role in historical consciousness.  
  
Tags: analog[^5] | bits[^6] | digital history[^7] | digitization[^8] | information theory[^9] | representation[^10]

[Back to the blog archive](../README.md)

[^1]: `http://groups.google.com/group/rec.puzzles/browse_thread/thread/2fb8426d9da1fea0/`
[^2]: `http://www.amazon.com/Programming-Universe-Quantum-Computer-Scientist/dp/1400040922/`
[^3]: `http://nora.lis.uiuc.edu/xtf/view?docId=blackwell/9781405103213/9781405103213.xml&chunk.id=ss1-1-2&toc.depth=1&toc.id=ss1-1-2&brand=default`
[^4]: `http://cdli.ucla.edu/`
[^5]: `http://technorati.com/tag/analog`
[^6]: `http://technorati.com/tag/bits`
[^7]: `http://technorati.com/tag/digital+history`
[^8]: `http://technorati.com/tag/digitization`
[^9]: `http://technorati.com/tag/information+theory`
[^10]: `http://technorati.com/tag/representation`
