available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "table",
                   "hdmi",
                   "dvd drive"]
#valid_choices = [str(i) for i in range (1,len(available_parts) +1)] #considers the length of list and add 1 for every iteration until the number reaches the length of list
valid_choices = []
for i in range(1 , len(available_parts) + 1) :
    valid_choices.append(str(i))
print(valid_choices)
current_choice = '-'
computer_parts = [] #create an empty list

while current_choice != '0' :
    if current_choice in valid_choices :
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts :
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else :
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains : {}".format(computer_parts))
    else :
        print("Please add options from the list below : ")
        for number, i in enumerate(available_parts) :
            print("{0} : {1}".format(number + 1, i))
            
    current_choice = input()
print(computer_parts)