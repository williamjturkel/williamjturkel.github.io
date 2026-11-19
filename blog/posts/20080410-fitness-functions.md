# Fitness Functions

_April 10, 2008_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2008/04/fitness-functions.html`

[Cross-posted to Cliopatria & Digital History Hacks]  

One of the distinctions that applied mathematicians make is between linear and nonlinear problems. In a linear problem, you have a set of variables that you can tweak, and as you adjust each variable you can get ever closer to an optimal configuration. Using techniques such as linear programming[^1], it is straightforward to determine precisely how many scoops of raisins to put in your box of bran, or how many Cherries will make a Garcia. Many problems, alas, don't admit of this kind of solution. In the days before digital everything, it was all too common to futz around with the brightness knob, color balance, rabbit ears, and position of pets and small children to try and get a TV signal that didn't look like it was being relayed from the dark side of the moon. The slightest change could make things drastically better or worse, with no apparent logic.  

The problem with nonlinear problems is that you pretty much have to get every variable right at the same time. Think of the space of all possible states of your problem as a kind of dark landscape, and the optimal solution as the highest point in that space. Linear problems have smooth landscapes. If you start groping your way up a hill, you end up at the top and that's the best you can do overall. Nonlinear problems have jagged landscapes. It is easy to feel your way up a low peak and get stuck there, unaware of higher peaks elsewhere.  

There are different methods for solving nonlinear optimization problems; one of the more popular makes use of genetic algorithms[^2]. First you find a way of representing all of the possible solutions to your problem. In the TV example, you might want to represent the angle of each of the two antennas, the xy coordinates of the napping cat, the rotational angle of the brightness knob, and so on. A list of each of these variables is known as a genome, and a list of particular values as a genotype. Generate a small random population of genotypes, and test each one to see how good it is. This test is called the fitness function. In our example, it is the person sitting on the couch shouting "not bad," "pretty good" or "awful" each time an adjustment is made. Once you know how well each of your solutions performed, you make a new generation of solutions by mutating and recombining the genomes of your old ones. Over time, the fitness of the population increases, and the artificial selection mechanism eventually finds solutions that are near optimal. (If you want to start programming your own GAs, I recommend Mitchell's Introduction[^3] and Goldberg's Genetic Algorithms[^4] as good places to start).  

One of the perennial tragedies of academia is that we constantly pretend that our careers or those of our students are linear optimization problems. Grades are the most obvious way that we do this. Students learn that their mark on one test is independent of their mark on another, that it is better to have a high GPA than to risk taking hard courses that interest them, that exploration and failure will usually be punished. Teachers justify marks by appealing to rubrics, bemoaning grade inflation and students "who look good on paper." Too many of us think of a good career in terms of lines on a CV, a list of so many independent accomplishments, each of which can be attained and then forgotten.  

On a rainy day in 1992, I wandered into a Vancouver technical bookstore on my way home from school. I think I was probably avoiding a problem set or some other homework, as I've never been very good at doing what I should be doing rather than what I want to be doing. Anyway, I remember finding a copy of John Holland's Adaptation in Natural and Artificial Systems[^5] on the shelf of new releases and really wanting to buy it. I stood in the store holding the book for the longest time. It was more than I could afford, it was a distraction from my school work, I had a bad habit of buying books and losing interest in them. I had been doing a lot of exploring and a fair bit of failing. I finally made the decision that was, in context at least, sub-optimal. I bought the book and went home to read it rather than doing my schoolwork.  

I often tell my students that they should follow their curiosity, take chances and not be afraid to fail. You never really know what whim, what chance encounter or distraction is going to change your life. In my case, I read a lot of science fiction and graphic novels and ate a lot of guacamole. I played role playing games and got married early and happily. I watched TV. I got bad grades in linear algebra and analysis, but I liked math enough to keep trying until I got better at it. And my first published work was on a subject that was novel and trendy enough that my reputation as an up-and-coming researcher outweighed my uneven transcript: genetic algorithms. It's tempting to look back at that moment in the bookstore as a crucial inflection point in my life, but that would be too linear. The choices that we make affect our fitness, but never in a way that makes it easy to assign credit or blame.  

Tags: feedback[^6] \| genetic algorithms[^7] \| nonlinear optimization[^8] \| pedagogy[^9]

---

Previous: [Visualizing the Emergence of a Strategic Knowledge Cluster](20080405-visualizing-emergence-of-strategic.md)  
Next: [The Programming Historian is Now Available](20080504-programming-historian-is-now-available.md)  
[Back to the blog archive](../README.md)

[^1]: `http://en.wikipedia.org/wiki/Linear_programming`
[^2]: `http://www.aaai.org/AITopics/pmwiki/pmwiki.php/AITopics/GeneticAlgorithms`
[^3]: `http://www.amazon.com/Introduction-Genetic-Algorithms-Complex-Adaptive/dp/0262631857/`
[^4]: `http://www.amazon.com/Genetic-Algorithms-Optimization-Machine-Learning/dp/0201157675/`
[^5]: `http://www.amazon.com/Adaptation-Natural-Artificial-Systems-Introductory/dp/0262581116/`
[^6]: `http://technorati.com/tag/feedback`
[^7]: `http://technorati.com/tag/genetic+algorithms`
[^8]: `http://technorati.com/tag/nonlinear+optimization`
[^9]: `http://technorati.com/tag/pedagogy`
