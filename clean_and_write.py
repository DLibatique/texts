def clean_text(text):
    '''
    input: raw text
    output: text all lowercase and without punctuation
    '''
    
    #lowercase the entire text
    text = text.lower()

    #remove punctuation
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        text = text.replace(marker,'')

    #remove indents and extra spaces
    spaces = ['    ','     ','      ','               ']
    for element in spaces:
    	text = text.replace(element,'')

    #remove line numbers
    numbers = '1234567890'
    for number in numbers:
        text = text.replace(number,'')

    return text

def read_file(filename):
    '''
    input: filename
    output: raw text
    '''
    infile = open(filename)
    text = infile.read()
    infile.close()
    return text

def select_file(raw_file,clean_file):
    
    old_text = read_file(raw_file)

    #clean the text
    new_text = clean_text(old_text)

    #write to new file
    outfile = open(clean_file, mode='w')
    outfile.write(new_text)
    outfile.close()

def create_dictionary(filename):

    #get text and split at each new line
    raw_text = read_file(filename)
    line_list = raw_text.split('\n')

    #create dictionary and assign line to line number
    dict = {}
    for line_number, text in enumerate(line_list):
        dict[line_number+1] = text

    return dict

def vocab_set(filename):

    text = sorted(set(read_file(filename).split()))
    
    return text