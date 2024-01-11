def is_palindrome(string) :
    #backwards = string[::-1]
    #return backwards == string
    return string[::-1].casefold() == string.casefold()


def palidrome_sentence(sentence):
    string=''
    for char in sentence :
        if char.isalnum():
            string += char
    return string[::-1].casefold() == string.casefold()


word = input('Please enter a words to check: ')
if palidrome_sentence(word) :
    print('{} is a palidrome'.format(word))
else :
    print('{} is not a palidrome'.format(word))