emptyList = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)
sortedNumbers = sorted(numbers)
print(sortedNumbers)

digits = list("432985617")
print(digits)

moreNumbers = list(numbers) #By using list() we create another list and which holds different id from the other list.
moreNumbers = numbers[:] #Does the exact same thing as list() creates a new list
moreNumbers = numbers.copy() #Does the same as above methods
print(moreNumbers)
print(numbers is moreNumbers)
print(numbers == moreNumbers)