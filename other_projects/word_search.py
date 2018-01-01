import re
import clean_and_write
import os

def create_dictionary(filename):

    #get text and split at each new line
    raw_text = clean_and_write.read_file(filename)
    line_list = raw_text.split('\n')

    #create dictionary and assign line to line number
    dict = {}
    for line_number, text in enumerate(line_list):
        dict[line_number+1] = text

    return dict

def word_search(expression,dict):
	
    #define the regex expression you're searching
    test = expression

    #search for the expression in the values of a given dictionary, print initial match location
    for key,value in dict.items():
        if re.search(test,value):
            match = re.search(test,value)
            print "at line %s from index %s to %s" % (key,match.start(),match.end())
        else:
            pass

for file in os.listdir('clean_texts'):
    print "In %s, your expression was found:" % (file)
    word_search(r'clar[aiou][emrs]?(um)?',create_dictionary('clean_texts//'+file))