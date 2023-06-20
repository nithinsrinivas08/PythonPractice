userInput = input("Please enter 3 numbers : ")
stringTokens = userInput.split(",")
intTokens = []
for i in stringTokens :
    intTokens.append(int(i))

a,b,c = intTokens
result = a + b - c
print(result)