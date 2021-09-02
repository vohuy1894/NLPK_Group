from bs4 import BeautifulSoup
import matplotlib
import urllib.request

import nltk

from nltk.corpus import stopwords

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')

html = response.read()

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()]

clean_tokens = tokens[:]

sr = stopwords.words('english')

# Remove stopwords from file
for token in tokens:
    if token in sr:
        clean_tokens.remove(token)

# Add frequency to dictionary
freq = nltk.FreqDist(clean_tokens)

# Remove value of a key less than 5
for key, values in list(freq.items()):
    if values < 5:
        del freq[key]

# sorting the high frequency words
sorted(freq.items(), key=lambda item: item[1], reverse=True)  

# print top 10 distribution words
freq.plot(10, cumulative=False)  # print 10 high frequency keywords
