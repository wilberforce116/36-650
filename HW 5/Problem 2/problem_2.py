### Problem 2

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = "Hello in 36-650, & other MSP courses."
def remove_punctuation(input):
    output = ""
    for character in input:
        if character not in punctuations:
            output += character
    return(output)
remove_punctuation(text)


