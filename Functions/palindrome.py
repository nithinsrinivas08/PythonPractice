def isPalindrome(string):
    backwards = string[::-1].casefold()
    return backwards == string.casefold()

word = input("Please enter a word : ")
if isPalindrome(word):
    print("'{}' is a Palindrome".format(word))
else :
    print("'{}' is not a palindrome".format(word))