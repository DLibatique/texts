import random

def quiz():

    verbs = [
        ['ἄγω', 'ἄξω', 'ἤγαγον', 'ἦχα', 'ἦγμαι','ἤχθην'],
        ['βαίνω', 'βήσομαι', 'ἔβην', 'βέβηκα', None, None],
        ['βάλλω', 'βαλῶ', 'ἔβαλον', 'βέβληκα', 'βέβλημαι', 'ἐβλήθην'],
        ['δίδωμι', 'δώσω', 'ἔδωκα', 'δέδωκα', 'δέδομαι', 'ἐδόθην'],
        ['ἔρχομαι', 'ἐλεύσομαι', 'ἦλθον', 'ἐλήλυθα', None, None],
        ['ἔχω', 'ἕξω', 'ἔσχον', 'ἔσχηκα', None, None],
        ['ἵστημι', 'στήσω', 'ἔστην/ἔστησα', 'ἕστηκα', 'ἕσταμαι', 'ἐστάθην']
    ]

    #choose a verb
    selected_verb = random.choice(verbs)
	
    #choose a principal part of said verb, 2nd through 6th
    random_pp = selected_verb[random.randint(1,5)]

    #ensure that random_pp is assigned to an actual verbal form
    while random_pp == None:
        random_pp = selected_verb[random.randint(1,5)]

    #ask user to answer
    answer = input('What is the first principal part of ' + random_pp + '? --> ')

    #if user is incorrect, prompt again
    while answer != selected_verb[0]:
        answer = input('Try again! --> ')
    else:
        print('Correct!')

quiz()
