# https://likegeeks.com/nlp-tutorial-using-python-nltk/

from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords
import matplotlib
stopwords.words('english')

target = 'http://php.net/'
response = urllib.request.urlopen(target)
html = response.read()
#print(html)
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
#print (text)
tokens = [t for t in text.split()]
#print(tokens)
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
	if token in stopwords.words('english'):
		clean_tokens.remove(token)

#freq = nltk.FreqDist(tokens)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
	print (str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
