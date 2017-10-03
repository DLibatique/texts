import clean_and_write

file_pairs = [
    ('raw_texts/ov_met_1_raw.txt','clean_texts/ov_met_1_clean.txt'),
    ('raw_texts/ov_met_2_raw.txt','clean_texts/ov_met_2_clean.txt'),
    ('raw_texts/ov_met_3_raw.txt','clean_texts/ov_met_3_clean.txt'),
    ('raw_texts/ov_met_4_raw.txt','clean_texts/ov_met_4_clean.txt'),
    ('raw_texts/ov_met_5_raw.txt','clean_texts/ov_met_5_clean.txt'),
    ('raw_texts/ov_met_6_raw.txt','clean_texts/ov_met_6_clean.txt'),
    ('raw_texts/ov_met_7_raw.txt','clean_texts/ov_met_7_clean.txt'),
    ('raw_texts/ov_met_8_raw.txt','clean_texts/ov_met_8_clean.txt'),
    ('raw_texts/ov_met_9_raw.txt','clean_texts/ov_met_9_clean.txt'),
    ('raw_texts/ov_met_10_raw.txt','clean_texts/ov_met_10_clean.txt'),
    ('raw_texts/ov_met_11_raw.txt','clean_texts/ov_met_11_clean.txt'),
    ('raw_texts/ov_met_12_raw.txt','clean_texts/ov_met_12_clean.txt'),
    ('raw_texts/ov_met_13_raw.txt','clean_texts/ov_met_13_clean.txt'),
    ('raw_texts/ov_met_14_raw.txt','clean_texts/ov_met_14_clean.txt'),
    ('raw_texts/ov_met_15_raw.txt','clean_texts/ov_met_15_clean.txt'),
]

for (x,y) in file_pairs:
	clean_and_write.select_file(x,y)

#comments below are just funky things I'm playing with
'''
#word frequency dictionary

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
