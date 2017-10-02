def clean_text(text):
    '''
    input: raw text
    output: text all lowercase and without punctuation
    '''
    text = text.lower()
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        text = text.replace(marker,'')
    return text