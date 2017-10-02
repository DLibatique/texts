import clean_and_write

file_pairs = [
    ('raw_texts/ov_met_1_raw.txt','clean_texts/ov_met_1_clean.txt'),
    ('raw_texts/ov_met_2_raw.txt','clean_texts/ov_met_2_clean.txt'),
    ('raw_texts/ov_met_3_raw.txt','clean_texts/ov_met_3_clean.txt'),
    ('raw_texts/ov_met_4_raw.txt','clean_texts/ov_met_4_clean.txt'),
    ('raw_texts/ov_met_5_raw.txt','clean_texts/ov_met_5_clean.txt'),
    ('raw_texts/ov_met_6_raw.txt','clean_texts/ov_met_6_clean.txt')
]

for (x,y) in file_pairs:
	clean_and_write.select_file(x,y)

#comments below are just funky things I'm playing with
'''
words = text.split()
unique_words = set(words)


def count_in_list(item_to_count, list_to_search):
	number_of_hits = 0
	for item in list_to_search:
		if item == item_to_count:
			number_of_hits += 1
	return number_of_hits

word_frequency = {}
for word in unique_words:
	word_frequency[word] = count_in_list(word,words)

print word_frequency
print word_frequency['et']
'''
