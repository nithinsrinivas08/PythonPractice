available_parts = ["Computers",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse Pad",
                   "hdmi",
                   "Hard disk"]
# valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
valid_choices = []
for i in range(1, len(available_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = '-'
computer_parts = []
while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice)-1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {0}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {0}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains : {}".format(computer_parts))
    else:
        print('Please add options from below list :')
        for number, parts in enumerate(available_parts):
            print("{0}: {1}".format(number+1, parts))
    current_choice = input()
print(computer_parts)
