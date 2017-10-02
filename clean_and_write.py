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
    spaces = ['     ','      ','               ']
    for element in spaces:
    	text = text.replace(element,'')
	#remove line numbers
	numbers = '1234567890'
	for number in numbers:
		text = text.replace(number,'')
    return text

def select_file(raw_file,clean_file):
    #open the file, assign raw text to text variable
    infile = open(raw_file)
    text = infile.read()
    infile.close()
    #clean the text
    text = clean_text(text)
    #write to new file
    outfile = open(clean_file, mode='w')
    outfile.write(text)
    outfile.close()