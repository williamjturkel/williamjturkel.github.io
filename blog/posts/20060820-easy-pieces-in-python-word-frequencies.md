# Easy Pieces in Python: Word Frequencies

_August 20, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/easy-pieces-in-python-word-frequencies.html`

I had originally planned to use Perl with my digital history students but have come to the reluctant conclusion that the language probably isn't ideal for my purposes. Perl has the motto that "there's more than one way to do it," which is fine for experienced programmers but a bit confusing for beginners. So I've made the shift to Python[^1] and am very happy so far. When I came across the tutorial on word frequencies[^2] in Ruby at Semantic Humanities[^3], I decided it would make a nice demo for Python, too.  

The basic problem is to split a text file into an array of words, count the number of occurrences of each word, and return a dictionary sorted by frequency. For my text, I chose Charles William Colby, The Fighting Governor: A Chronicle of Frontenac[^4] (1915) available from Project Gutenberg. We start by reading the file into one long string and then use whitespace to split the string into a list of separate words. In Python it looks like this:  

```python
input = open('cca0710-trimmed.txt', 'r')
text = input.read()
wordlist = text.split()
```

or like this if you want to show off:  

```python
wordlist = open('cca0710-trimmed.txt', 'r').read().split()
```

Now that we have our word list, the next step is to create the dictionary. We do this first by counting the number of occurrences of each word in the list:  

```python
wordfreq = [wordlist.count(p) for p in wordlist]
```

Then we pair each word with its corresponding frequency to create the dictionary:  

```python
dictionary = dict(zip(wordlist,wordfreq))
```

Now that we have the dictionary, we can sort it by inverse word frequency and print out the results:  

```python
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()
for a in aux: print a
```

This gives us results like the following:  

```
(2574, 'the')
(1394, 'of')
(880, 'to')
(855, 'and')
(572, 'in')
(548, 'was')
(545, 'a')
(420, 'his')
...
(213, 'for')
(212, 'Frontenac')
(209, 'by')
(194, 'not')
...
(76, 'would')
(75, 'Iroquois')
(74, 'upon')
...
(68, 'English')
(68, 'Canada')
(66, 'New')
(65, 'France')
...
```

Not too hard, eh?  

Tags: programming[^5] \| python[^6] \| statistical natural language processing[^7] \| text mining[^8]

---

Previous: [Google as Corpus](20060810-google-as-corpus.md)  
Next: [Easy Pieces in Python: Keyword in Context](20060821-easy-pieces-in-python-keyword-in.md)  
[Back to the blog archive](../README.md)

[^1]: `http://www.python.org`
[^2]: `http://semantichumanities.wordpress.com/2006/02/21/word-frequencies-in-ruby-tutorial/`
[^3]: `http://semantichumanities.wordpress.com/`
[^4]: `http://www.gutenberg.org/dirs/etext04/cca0710.txt`
[^5]: `http://technorati.com/tag/programming`
[^6]: `http://technorati.com/tag/python`
[^7]: `http://technorati.com/tag/statistical+natural+language+processing`
[^8]: `http://technorati.com/tag/text+mining`
