# Easy Pieces in Python: Keyword in Context

_August 21, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/easy-pieces-in-python-keyword-in.html`

Yesterday, I showed that it is possible to extract useful information from a historical source (word frequencies) with a few lines of a high-level programming language like Python[^1]. Today we continue with another simple demo, keyword in context (KWIC[^2]). The basic problem is to split a text into a long list of words, slide a fixed window over the list to find n-grams[^3] and then put each n-gram into a dictionary so we can find the contexts for any given word in the text.  

As before, we are going to be working with Charles William Colby's *The Fighting Governor: A Chronicle of Frontenac[^4]* (1915) from Project Gutenberg. We start by reading the text file into a long string and then splitting it into a list of words:  

```python
wordlist = open('cca0710-trimmed.txt', 'r').read().split()
```

Next we run a sliding window over the word list to create a list of n-grams. In this case we are going to be using a window of five words, which will give us two words of context on either side of our keyword.  

```python
ngrams = [wordlist[i:i+5] for i in range(len(wordlist)-4)]
```

We then need to put each n-gram into a dictionary, indexed by the middle word. Since we are using 5-grams, and since Python sequences are numbered starting from zero, we want to use 2 for the index.  

```python
kwicdict = {}
for n in ngrams:
    if n[2] not in kwicdict:
        kwicdict[n[2]] = [n]
    else:
        kwicdict[n[2]].append(n)
```

Finally, we will want to do a bit of formatting so that our results are printed in a way that is easy to read. The code below gets all of the contexts for the keyword 'Iroquois'.  

```python
for n in kwicdict['Iroquois']:
    outstring = ' '.join(n[:2]).rjust(20)
    outstring += str(n[2]).center(len(n[2])+6)
    outstring += ' '.join(n[3:])
    print outstring
```

This gives us the following results.  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| bears, and |  | Iroquois |  | knew that |
| of the |  | Iroquois |  | villages. At |
| with the |  | Iroquois |  | at Cataraqui |
| to the |  | Iroquois |  | early in |
| to the |  | Iroquois |  | chiefs, Frontenac |
| shelter the |  | Iroquois |  | from the |
| wished the |  | Iroquois |  | to see |
| of the |  | Iroquois |  | a fort |
|  |  | ... |  |  |
| that captured |  | Iroquois |  | were burned |

This kind of analysis can be useful for historiographical argumentation. If we look at the contexts in which the Iroquois appear in Colby's text, we find that they are usually the objects of verbs rather than the subjects. That is to say that we find a lot of phrases like "to the Iroquois," "make the Iroquois," "overawe the Iroquois," "invite the Iroquois," "with the Iroquois," "smiting the Iroquois," and so on. We find far fewer phrases of the form "[the] Iroquois knew," "the Iroquois rejoiced," or "six hundred Iroquois invaded." This could be taken to suggest that Colby wasn't thinking of the Iroquois as historical agents (which is how most historians see them now) but rather as background characters, as foils for the settlers of New France.  

Tags: concordance[^5] \| KWIC[^6] \| n-grams[^7] \| programming[^8] \| python[^9] \| text mining[^10]

---

Previous: [Easy Pieces in Python: Word Frequencies](20060820-easy-pieces-in-python-word-frequencies.md)  
Next: [Easy Pieces in Python: Removing Stop Words](20060823-easy-pieces-in-python-removing-stop.md)  
[Back to the blog archive](../README.md)

[^1]: `http://www.python.org`
[^2]: `http://en.wikipedia.org/wiki/KWIC`
[^3]: `http://en.wikipedia.org/wiki/N-gram`
[^4]: `http://www.gutenberg.org/dirs/etext04/cca0710.txt`
[^5]: `http://technorati.com/tag/concordance`
[^6]: `http://technorati.com/tag/kwic`
[^7]: `http://technorati.com/tag/ngrams`
[^8]: `http://technorati.com/tag/programming`
[^9]: `http://technorati.com/tag/python`
[^10]: `http://technorati.com/tag/text+mining`
