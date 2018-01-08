import re
import clean_and_write
import os

def word_search(expression,dict):
	
    #define the regex expression you're searching
    test = expression

    #search for the expression in the values of a given dictionary
    for key,value in dict.items():

        if re.search(test,value):

            match = re.search(test,value)

            #print initial match location
            print("at line %s from index %s to %s" % (key,match.start(),match.end()))

            #print passage for context
            for line in range(max(1, key-5), min(len(dict), key+6)):
                print(dict[line])
            print("\n")

        else:
            pass

#determine set of texts to search
ordered_files = sorted(os.listdir('clean_texts'), key=lambda x: (int(re.sub('\D','',x)),x))

#search within texts
for file in ordered_files:
    print("In %s, clarus, -a, -um was found:" % (file))
    word_search(r'clar[aiou][emrs]?(um)?',clean_and_write.create_dictionary('clean_texts//'+file))