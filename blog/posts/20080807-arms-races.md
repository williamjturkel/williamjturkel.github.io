# Arms Races

_August 7, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/08/arms-races.html`

[Cross-posted to Cliopatria and Digital History Hacks]  

Like many people who blog at Blogger, I was recently notified by e-mail that my blog had been identified by their automated classifiers "as a potential spam blog." In order to prove that this was not the case, I had to log in to one of their servers and request that my blog be reviewed by a human being. The e-mail went on to say "Automatic spam detection is inherently fuzzy, and occasionally a blog like yours is flagged incorrectly. We sincerely apologize for this error." The author of the e-mail knew, of course, that if my blog were sending spam then his or her e-mail would fall on deaf ears (as it were)... you don't have to worry about bots' feelings. The politeness was intended for me, a hapless human caught in the crossfire in the war of intelligent machines[^1].  

That same week, a lot of my e-mails were also getting bounced. Since I have my blog address in my .sig file, I'm guessing that may have something to do with it. Alternately, my e-mail address may have been temporarily blocked as the result of a surge in spam being sent from GMail servers. This to-and-fro, attack against counter-attack, *Spy vs. Spy*[^2] kind of thing can be irritating for the collaterally damaged but it is good news for digital historians, as paradoxical as that may seem.  

One of the side effects of the war on spam has been a lot of sophisticated research on automated classifiers that use Bayesian or other techniques to categorize natural language documents. Historians can use these algorithms to make their own online archival research much more productive, as I argued in a series of posts[^3] this summer.  

In fact, a closely related arms race is being fought at another level, one that also has important implications for the digital humanities. The optical character recognition (OCR) software that is used to digitize paper books and documents is also being used by spammers to try and circumvent software intended to block them. This, in turn, is having a positive effect on the development of OCR algorithms, and leading to higher quality digital repositories as a collateral benefit. Here's how.  

* Computer scientists create the CAPTCHA[^4], a "Completely Automated Public Turing test to tell Computers and Humans Apart." In essence, it shows a wonky image of a short text on the screen, and the (presumably human) user has to read it and type in the characters. If they match, the system assumes a real person is interacting with it.
* Google releases the Tesseract OCR engine[^5] that they use for Google Books as open source. On the plus side, a whole community of programmers can now improve Tesseract OCR. On the minus side, a whole community of spammers can put it to work cracking CAPTCHAs.
* In the meantime, a group of computer scientists comes up with a brilliant idea, the reCAPTCHA[^6]. Every day, tens of millions of people are reading wonky images of short character strings and retyping them. Why not use all of these infinitesimal units of labor to do something useful? The reCAPTCHA system uses OCR errors for its CAPTCHAs. When you respond to a reCAPTCHA challenge, you're helping to improve the quality of digitized books.
* The guys with white hats[^7] are also using OCR to crack CAPTCHAs, with the aim of creating stronger challenges. One side effect is that the OCR gets better at recognizing wonky text, and thus better for creating digital books.

Tags: machine learning[^8] \| optical character recognition (OCR)[^9] \| Turing test[^10]

---

Previous: [Towards a Computational History](20080720-towards-computational-history.md)  
Next: [Traces of Use](20080820-traces-of-use.md)  
[Back to the blog archive](../README.md)

[^1]: `http://www.amazon.com/War-Intelligent-Machines-Manuel-Landa/dp/0942299752/`
[^2]: `http://www.amazon.com/Spy-vs-Complete-Casebook/dp/0823050211/`
[^3]: `http://digitalhistoryhacks.blogspot.com/search?q=bayesian`
[^4]: `http://en.wikipedia.org/wiki/Captcha`
[^5]: `http://google-code-updates.blogspot.com/2006/08/announcing-tesseract-ocr.html`
[^6]: `http://recaptcha.net/`
[^7]: `http://en.wikipedia.org/wiki/White_hat`
[^8]: `http://technorati.com/tag/machine+learning`
[^9]: `http://technorati.com/tag/optical+character+recognition`
[^10]: `http://technorati.com/tag/turing+test`
