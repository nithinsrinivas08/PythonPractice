import random


def get_integer(prompt):
    """
    Get an integer from standard Inout (stdin)
    The function will continue looping, and prompting.
    the user, until a valid `int` is entered.
    :param prompt : The string that the user will see, when they're prompted to enter the value
    :return : The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else :
        print("{} is not a valid number".format(temp))


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
# print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

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
