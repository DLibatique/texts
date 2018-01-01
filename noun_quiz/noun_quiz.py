nouns = ['θεός']

second_decl_endings = ['ός', 'οῦ', 'ῷ', 'όν', 'οί', 'ῶν', 'οῖς', 'ούς']

inflected = []

for noun in nouns:

	for ending in second_decl_endings:

		noun = noun[0:2] + ending
		inflected.append(noun)

print(inflected)

