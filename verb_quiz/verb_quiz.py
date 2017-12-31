import random

verbs = {
    'ἄγω':['ἄξω', 'ἤγαγον', 'ἦχα', 'ἦγμαι','ἤχθην'],
    'βαίνω':['βήσομαι', 'ἔβην', 'βέβηκα', None, None],
    'βάλλω':['βαλῶ', 'ἔβαλον', 'βέβληκα', 'βέβλημαι', 'ἐβλήθην'],
    'δίδωμι':['δώσω', 'ἔδωκα', 'δέδωκα', 'δέδομαι', 'ἐδόθην'],
    'ἔρχομαι':['ἐλεύσομαι', 'ἦλθον', 'ἐλήλυθα', None, None],
    'ἔχω':['ἕξω', 'ἔσχον', 'ἔσχηκα', None, None],
    'ἵστημι':['στήσω', 'ἔστην/ἔστησα', 'ἕστηκα', 'ἕσταμαι', 'ἐστάθην']
}

#group the verbs' 2nd through 6th principal parts
principal_parts = list(verbs.values())

#choose random principal part from random verb
random_principal_part = random.choice(principal_parts[random.randint(0,4)])

#prompt to quiz taker
print('What is the first principal part of', random_principal_part, '?')

