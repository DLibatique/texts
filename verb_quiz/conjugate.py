def simple_conjugate(stem, ending_list):

	finished_list = []

	for ending in ending_list:

		verb = stem + ending
		finished_list.append(verb)

	return finished_list

def full_conjugate(verb):

	full_list = []

	for pair in verb:
	
		full_list.extend(simple_conjugate(pair[0], pair[1]))

	return full_list