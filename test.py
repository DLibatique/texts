import clean_text

infile = open('met_1.txt')
text = infile.read()
infile.close()

text = clean_text.clean_text(text)
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
