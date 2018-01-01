import random

def quiz():

    verbs = [
        ['ἄγω', 'ἄξω', 'ἤγαγον', 'ἦχα', 'ἦγμαι','ἤχθην'],
        ['βαίνω', 'βήσομαι', 'ἔβην', 'βέβηκα', None, None],
        ['βάλλω', 'βαλῶ', 'ἔβαλον', 'βέβληκα', 'βέβλημαι', 'ἐβλήθην'],
        ['δίδωμι', 'δώσω', 'ἔδωκα', 'δέδωκα', 'δέδομαι', 'ἐδόθην'],
        ['ἔρχομαι', 'ἐλεύσομαι', 'ἦλθον', 'ἐλήλυθα', None, None],
        ['ἔχω', 'ἕξω', 'ἔσχον', 'ἔσχηκα', None, None],
        ['ἵστημι', 'στήσω', 'ἔστην/ἔστησα', 'ἕστηκα', 'ἕσταμαι', 'ἐστάθην'],
        ['ὁράω', 'ὄψομαι', 'εἶδον', 'ἑώρακα', 'ὦμμαι', 'ὤφθην'],
        ['τίθημι', 'θήσω', 'ἔθηκα', 'τέθεικα', 'τέθειμαι', 'ἐτέθην'],
        ['φημί', 'φήσω', 'ἔφησα', None, None, None]
    ]

    verbs = random.sample(verbs, len(verbs))

    no_of_questions = input('How many verbs would you like to quiz yourself on? --> ')

    while int(no_of_questions) > len(verbs):
        no_of_questions = input('You can choose up to ' + str(len(verbs)) + ' verbs. Choose again! --> ')

    for verb in verbs[0:int(no_of_questions)]:

        random_pp = verb[random.randint(1,5)]

        while random_pp == None:
            random_pp = verb[random.randint(1,5)]

        answer = input('What is the first principal part of ' + random_pp + '? --> ')

        while answer != verb[0]:
            answer = input('Try again! --> ')
        else:
            print('Correct!')
            pass

quiz()
