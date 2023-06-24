def multiply(x,y):
    """
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result

answer = multiply(10.5,4)
print(answer)

fortyTwo = multiply(6,7)
print(fortyTwo)

for i in range(1,5) :
    sol = multiply(2,i)
    print(sol)