import nltk
import clean_and_write
import re

'''
print 'scelus' in clean_and_write.vocab_set('clean_texts/ov_met_6_clean.txt')

met6 = clean_and_write.read_file('clean_texts/ov_met_6_clean.txt').split()


fdist1 = nltk.FreqDist(met6)
print fdist1.most_common(50)
fdist1.plot(50, cumulative=True)
print fdist1.hapaxes()

V = set(met6)
long_words = [word for word in V if len(word) > 10]
print sorted(long_words)


print list(nltk.bigrams(met6))


fdist1 = nltk.FreqDist(met6)
print fdist1['intendens']


word comparison operators:
s.startswith(t)
s.endswith(t)
t in s (is t a substring of s?)
s.islower() (all lowercase)
s.isupper() (all caps)
s.isalpha() (alphabetic)
s.isalnum() (alphanumeric)
s.isdigit() (numbers)
s.istitle() (titlecased)


print ['Monty','Python'] * 20

print ' '.join(met6)
'''

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print emma.concordance("surprize")