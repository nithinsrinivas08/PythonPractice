data = [4,5,104,105,110,120,130,150,213,234,2345,1234,3200,3454]
print(len(data))
#DELETE ITEM FROM LIST
del data[0:2]
print(data)
print(len(data))

#DELETE THE VLAUES BETWEEN RANGES
min_valid = 100
max_valid = 3000
for i,value in enumerate(data) :
    if (value < min_valid) or (value > max_valid) :
        del data[i] #THIS WAY WE MISS OUT FEW VALUES BECAUSE OF ITS LIMITATION
print(data)

#ANOTHER METHOD
min_valid = 100
max_valid = 3000
#PROCESS THE LOW VALUES IN THE LIST
stop = 0
for i, value in enumerate(data) :
    if value >= min_valid :
        stop = i
        break
print(stop) #FOR DEBUGGING
del data[:stop]
print(data)

#PROCESS THE HIGH VALUES IN THE LIST
start = 0
for i in range(len(data) -1, -1, -1) :
    if data[i] <= max_valid:
        #WE HAVE THE INDEX OF THE LAST ITEM TO KEEP
        #SET 'START' TO THE POSITION OF THE FIRST
        # ITEM TO DELETE, WHICH IS 1 AFTER 'I'  
        start = i + 1
        break
print(start)
del data[start:]
print(data)