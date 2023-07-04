def fizzBuzz(number : int) -> str :
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0 :
        return "fizz"
    elif number % 5 == 0 :
        return "buzz"
    else :
        return str(number)

input("Play Fizz Buzz. Press ENTER to start")
print()
nextNumber = 0
while nextNumber<99 :
    nextNumber += 1
    print(fizzBuzz(nextNumber))
    nextNumber += 1
    correctAnswer = fizzBuzz(nextNumber)
    playersAnswer = input("Your go : ")
    if playersAnswer != correctAnswer :
        print("You lose, the correct answer was {}".format(correctAnswer))
        break
else :
    print("Well done, you reached {}".format(nextNumber))