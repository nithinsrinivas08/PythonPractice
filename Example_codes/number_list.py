even = [2,4,6,8]
odd = [1,3,5,7,9]

print(min(even))
print(max(odd))
print(len(even))
print(len(odd))

even.extend(odd)
even.sort(reverse = True)
print(even)