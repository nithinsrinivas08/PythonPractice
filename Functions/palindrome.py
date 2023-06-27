def isPalindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
 
    A palindrome is a string that reads the same forwards as backwards.
 
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    backwards = string[::-1].casefold()
    return backwards == string.casefold()

word = input("Please enter a word : ")
if isPalindrome(word):
    print("'{}' is a Palindrome".format(word))
else :
    print("'{}' is not a palindrome".format(word))

p=isPalindrome()