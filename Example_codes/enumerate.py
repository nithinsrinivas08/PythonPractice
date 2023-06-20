for index, character in enumerate("abcdefgh") :
    print(index, character)

#EXPLAINING ENUMERATE
for t in enumerate("abcdefgh") :
    print(t) #WE CAN LOO AT THE RESULT AS IT GIVES THE INDEX AND CHARAC OF THE STRING ASSIGNED TO ENUMERATE

#ASSIGN INDEX AND CHARAC (UNPACK TUPLE)
for t in enumerate("abcdefgh") :
    i,c = t
    print(i,c) #FOR EACH LOOP INSTANCE IT GIVES THE INDEX AND CHARAC