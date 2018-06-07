# https://likegeeks.com/nlp-tutorial-using-python-nltk/

from nltk.tokenize import sent_tokenize, word_tokenize
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
#print(sent_tokenize(mytext))
print(word_tokenize(mytext))

myfrenchtext = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
print(sent_tokenize(myfrenchtext,"french"))

from nltk.corpus import wordnet
print("WordNet examples of 'NLP':")
syn = wordnet.synsets("NLP")
print(syn[0].definition())
print(syn[0].examples())
print("WordNet examples of 'Python':")
syn = wordnet.synsets("Python")
print(syn[0].definition())
print(syn[0].examples())

print("Synonyms of 'Computer':")
synonyms = []
for syn in wordnet.synsets('Computer'):
	for lemma in syn.lemmas():
		synonyms.append(lemma.name())
print(synonyms)

print("Antonyms of 'small':")
antonyms = []
for syn in wordnet.synsets("small"):
	for l in syn.lemmas():
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())
print(antonyms)

print("Word Stemming of 'working':")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))