import nltk
import matplotlib
from nltk.corpus import stopwords

# -----------------------------------
import sys              # Using 'sys.argv' and 'sys.exit()'
num_words = num_lines = num_chars = 0  # chain assignment
 
with open('resume.txt', encoding='utf-8', mode='r') as infile:
    for line in infile:           # Process each line (including newline) in a for-loop
        num_lines += 1            # No ++ operator in Python?!
        num_chars += len(line)
        line = line.strip()       # Remove leading and trailing whitespaces
        words = line.split()      # Split into a list using whitespace as delimiter
        num_words += len(words)
 
print('# Lines: %d' % num_lines)  # C-like printf()
print('# Words: %d' % num_words)
print('# Chars: %d' % num_chars)



read_data = []
with open('resume.txt', encoding='utf-8', mode='r') as datafile:
    for line in datafile:
        for word in line.split():
           read_data.append(word)
#print(read_data)

from collections import Counter
list1=read_data
counts = Counter(list1)
print(counts)
# Counter({'apple': 3, 'egg': 2, 'banana': 1})


import re
with open('resume.txt', encoding='utf-8', mode='r') as f1:
    for line in f1:
        for word in re.findall(r'\w+', line):
           read_data.append(word)

stopwords.words('english')
tokens = [t for t in read_data]
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
	if token in stopwords.words('english'):
		clean_tokens.remove(token)

freq = nltk.FreqDist(read_data)
for key,val in freq.items():
	print (str(key) + ':' + str(val))
freq.plot(20, cumulative=False)