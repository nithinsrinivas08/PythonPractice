import random

def getInteger(prompt) :
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else :
        print("{} is not a valid number".format(temp))
 
highest = 1000
answer = random.randint(1, highest)
#print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))
 
while guess != answer:
    guess = getInteger(": ")
 
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
