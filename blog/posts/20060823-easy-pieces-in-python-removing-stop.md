# Easy Pieces in Python: Removing Stop Words

_August 23, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/easy-pieces-in-python-removing-stop.html`

We continue our exploration of simple Python[^1] scripting with another common problem: removing stop words[^2]. About forty percent of a given text consists of very common words like 'a', 'the', 'and', etc. While necessary to convey meaning, these words don't distinguish the text from other texts, and thus are usually not very useful for tasks like searching, indexing, determining good keywords, and so on.  
  
As before, we are working with Charles William Colby's The Fighting Governor: A Chronicle of Frontenac[^3] (1915) from Project Gutenberg. We will also be using a list of stop words[^4] posted online by computer science researchers at Glasgow. For a specific research project, we would want to tune this list, but it is fine for demo purposes. As before, we read both of our text files into lists of words.  
 `textwords = open('cca0710-trimmed.txt', 'r').read().split()  
stopwords = open('stop_words.txt', 'r').read().split()`  
Now we have two options. If we want to maintain some semblance of context, we can replace each stop word with a marker[^5]. The following code does exactly that.  
 `markeredtext = []  
for t in textwords:  
    if t.lower() in stopwords:  
        markeredtext.append('*')  
    else:  
        markeredtext.append(t)`  
Before replacing stopwords with markers, a sentence from our file looks like this:  
> ['In', 'short,', 'the', 'divine', 'right', 'of', 'the', 'king', 'to', 'rule', 'over', 'his', 'people', 'was', 'proclaimed', 'as', 'loudly', 'in', 'the', 'colony', 'as', 'in', 'the', 'motherland.']

  
Afterwards, it looks like this:  
> ['\*', 'short,', '\*', 'divine', 'right', '\*', '\*', 'king', '\*', 'rule', '\*', '\*', 'people', '\*', 'proclaimed', '\*', 'loudly', '\*', '\*', 'colony', '\*', '\*', '\*', 'motherland.']

  
For other applications, we may not need to use markers. To simply delete stopwords, we can use the following code instead:  
 `filteredtext = [t for t in textwords if t.lower() not in stopwords]`  
This is what the same sentence looks like when stop words are deleted:  
> ['short,', 'divine', 'right', 'king', 'rule', 'people', 'proclaimed', 'loudly', 'colony', 'motherland.']

  
  
Tags: programming[^6] \| python[^7] \| text mining[^8]

[Back to the blog archive](../README.md)

[^1]: `http://www.python.org`
[^2]: `http://en.wikipedia.org/wiki/Stop_words`
[^3]: `http://www.gutenberg.org/dirs/etext04/cca0710.txt`
[^4]: `http://www.dcs.gla.ac.uk/idom/ir_resources/linguistic_utils/stop_words`
[^5]: `http://searchenginewatch.com/showPage.html?page=2156061`
[^6]: `http://technorati.com/tag/programming`
[^7]: `http://technorati.com/tag/python`
[^8]: `http://technorati.com/tag/text+mining`
