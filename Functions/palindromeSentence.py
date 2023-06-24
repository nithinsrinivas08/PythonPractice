def palindromeSentence(sentence) :
    """
    Check if a sentence is a palindrome.
 
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence :
        if char.isalnum() :
            string += char
    return string[::-1].casefold() == string.casefold()

word = input("Please enter a word or sentence : ")
if palindromeSentence(word) :
    print("'{}' is a palindrome".format(word))
else :
    print("'{}' is not a palindrome".format(word))