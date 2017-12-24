import random

def randomize(list):
	return random.choice(list)

nouns = [
	'ἄνθρωπος, ἀνθρώπου, ὁ',
	'ἀρχή, ἀρχῆς, ἡ',
	'βουλή, βουλῆς, ἡ',
	'γνώμη, γνώμης, ἡ',
	'δίκη, δίκης, ἡ'
]

print(randomize(nouns))