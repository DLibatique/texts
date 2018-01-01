
def simple_conjugate(stem, ending_list):

	finished_list = []

	for ending in ending_list:

		verb = stem + ending
		finished_list.append(verb)

	return finished_list