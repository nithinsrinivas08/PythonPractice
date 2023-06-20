def palindromeSentence(sentence) :
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