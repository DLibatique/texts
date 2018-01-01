'''
All code by Patrick Burns, @diyclassics. This is just for me to play around with!
'''
import clean_and_write

# Import word tokenizer & backoff lemmatizer

from cltk.tokenize.word import WordTokenizer
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer

# Set up training sentences from latin_models_cltk

import os
from cltk.utils.file_operations import open_pickle

rel_path = os.path.join('~/cltk_data/latin/model/latin_models_cltk/lemmata/backoff')
path = os.path.expanduser(rel_path)

# Check for presence of latin_pos_lemmatized_sents
file = 'latin_pos_lemmatized_sents.pickle'      

latin_pos_lemmatized_sents_path = os.path.join(path, file)
if os.path.isfile(latin_pos_lemmatized_sents_path):
    latin_pos_lemmatized_sents = open_pickle(latin_pos_lemmatized_sents_path)
else:
    latin_pos_lemmatized_sents = []
    print('The file %s is not available in cltk_data' % file)

# Set up CLTK tools

word_tokenizer = WordTokenizer('latin')
lemmatizer = BackoffLatinLemmatizer(latin_pos_lemmatized_sents)

# Get tokens

tokens = clean_and_write.vocab_set('clean_texts/ov_met_6_clean.txt')
print(tokens)

# Get lemmas

lemmas = lemmatizer.lemmatize(tokens)
print(lemmas)

lemmata = []
for (x,y) in lemmas:
	lemmata.append(y)
print(sorted(set(lemmata)))