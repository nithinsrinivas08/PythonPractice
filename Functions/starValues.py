numbers = (0,1,2,3,4,5)
print(numbers, sep=";")
print(*numbers, sep=";")
print(0,1,2,3,4,5, sep=";")

def testStar(*arg) :
    print(arg)
    for x in arg:
        print(x)

testStar(0,1,2,3,4,5)