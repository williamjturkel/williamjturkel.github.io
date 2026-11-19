# Putting It in Your Own Words

_July 31, 2007_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2007/07/putting-it-in-your-own-words.html`

When we teach history students how to take notes for research, we usually tell them to take down direct quotes sparingly, and to put things in their own words instead. Many university writing labs provide training in the art of paraphrasing[^1]. One concern is that direct quotes lend themselves to witting or unwitting plagiarism, especially if the paper is being written the night before it's due.  
  
I've always found paraphrasing to be an unsatisfactory exercise because it is in direct tension with close reading. You read the original passage carefully, set it to one side, and then write out the ideas in your own words. At that point you're supposed to re-read the original passage and make sure that you captured the essence. Of course you didn't. As Mark Twain once said, "The difference between the almost-right word & the right word is really a large matter -- it's the difference between the lightning-bug and the lightning." [\*[^2]] If a student came to me with this example, I'd tell them that there are times when you really should quote rather than paraphrase.  
  
In fact, when I'm taking notes, I usually write down a lot of direct quotes. When I go back to them later, I find that the author's exact words serve as much better reminders of his or her work than paraphrases do. And when I write my first draft of anything, I usually have a lot more quotes than I'm going to want to have in the final version. I know that I'm going to re-read and re-write each passage dozens of times, and that all but the best quotes will be squeezed out in the process.  
  
The problem of putting something in your own words is paralleled in machine learning by a problem known as overfitting. Suppose you work on the production line of a company that makes delicious little chocolates with multi-colored candy shells [Cdn[^3]\|US[^4]]. Even though all of the candies taste the same, your company has come to the conclusion that people pay attention to the color ... they have marketing campaigns based on a preference for eating the red ones last, or the ability to customize the color, or whatever. Your job is to look at the candies as they go by and sort them by color, tossing out any that don't match one of the approved shades. (Sometimes the coloring machine malfunctions and you end up with colors that are more appropriate to your competitor[^5].) Now any hacker in this situation is going to build a robot, so you do. As the candies come down the line, the robot tries to sort them and you provide feedback. If you don't provide enough training, the robot might decide that all of the candies are either blue or red. It is right some of the time, but not enough. That is known as underfitting. If you provide it with too much training on a limited set of examples, it might be correct 100 percent of the time for those examples, but at the cost of memorizing too much detail. Suppose you see five candies in a row, and categorize each as blue. To simplify quite a bit, things that we call "blue" have a wavelength around 475 nanometers. Your robot, however, comes up with five very specific rules: IF WAVELENGTH = 460.83429nm THEN COLOR = blue; IF WAVELENGTH = 483.00089nm THEN COLOR = blue; and so on. Once you turn it loose on a new batch of candies, it is going to start malfunctioning, because it learned too much detail about your original set of examples. It doesn't know what to do if the wavelength is 460.84000nm. This is the problem of overfitting. Now there are a lot of sophisticated methods[^6] for avoiding these problems if you are forced to model a limited data set. But the best way to avoid them is to use a lot of training data.  
  
Which brings us back to putting things in your own words. The problem that students encounter with note-taking doesn't have as much to do with quoting vs. paraphrasing as you might think. The problem has to do with not looking at enough sources. If you only consult a handful of sources, then direct quoting might lead you to plagiarism, which would be a case of overfitting. If you paraphrase a handful of sources instead, you may avoid plagiarism but your essay isn't going to be any more nuanced. That is going to lead to underfitting. Either way, a model of a small number of sources is bound to be a bad predictor for the sources that you didn't consult. The only way out is to read more... a lot more. (See my earlier post on "The Difference That Makes a Difference[^7].")  
  
Tags: convergence[^8] \| machine learning[^9] \| overfitting[^10] \| reading[^11] \| writing[^12]

[Back to the blog archive](../README.md)

[^1]: `http://owl.english.purdue.edu/handouts/research/r_paraphr.html`
[^2]: `http://www.amazon.com/Yale-Book-Quotations-Joseph-Epstein/dp/0300107986/`
[^3]: `http://www.nestle.ca/en/products/brands/smarties/index`
[^4]: `http://us.mms.com/us/`
[^5]: `http://jellybelly.com/Cultures/en-US/Shop/CandyDetails.htm?CS_ProductID=1064337&CS_Category=BertieBotts&CS_Catalog=B2C`
[^6]: `http://www.faqs.org/faqs/ai-faq/neural-nets/part3/section-3.html`
[^7]: `http://digitalhistoryhacks.blogspot.com/2006/11/difference-that-makes-difference.html`
[^8]: `http://technorati.com/tag/convergence`
[^9]: `http://technorati.com/tag/machine+learning`
[^10]: `http://technorati.com/tag/overfitting`
[^11]: `http://technorati.com/tag/reading`
[^12]: `http://technorati.com/tag/writing`
