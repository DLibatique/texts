import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def read_file(filename):
    '''
    input: filename
    output: raw text
    '''
    infile = open(filename)
    text = infile.read()
    infile.close()
    return text

def write_file(filename,text):
    #write to new file
    outfile = open(filename, mode='w')
    outfile.write(text)
    outfile.close()

def no_returns(text):
    
    text = text.replace('\n\n','\n')
    text = text.replace('\n[','\n\n[')

    return text

#write_file('iliad1notes_clean.txt', no_returns(read_file('iliad1notes.txt')))

print read_file('iliad1notes_clean.txt')