import clean_and_write

def word_frequency(filename):
	#get text to determine word frequency of, split into individual strings
	words = clean_and_write.read_file(filename).split()

	#create list of unique words
	unique_words = set(words)

	#create frequencies for each unique word
	def count(item,list):
		number_of_hits = 0
		for x in list:
			if x == item:
				number_of_hits += 1
		return number_of_hits

	#create dictionary
	word_frequency = {}
	for word in unique_words:
		word_frequency[word] = count(word,words)

	return word_frequency

print word_frequency('clean_texts/ov_met_6_clean.txt')['lacrimae']