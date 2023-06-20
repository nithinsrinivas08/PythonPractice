data = [104,105,4,101,308,103,5,107,100,306,106,102,108]
minValid = 100
maxValid = 200
for i in range(len(data) -1, -1, -1) :
    if data[i] < minValid or data[i] > maxValid :
        print(i, data)
        del data[i]
print(data)

#ANOTHER METHOD THAT CAN BE USED TO REMOVE DATA BETWEEN RANGE USING REVERSED() FUNCITON
topIndex = len(data) -1
for i,v in enumerate(reversed(data)) :
    if v < minValid or v > maxValid :
        print(topIndex - i, v)
        del data[topIndex - i]
print(data)   