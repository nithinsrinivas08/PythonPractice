computer_parts = ["computers",
                  "monitor",
                  "keyboard",
                  "mouse"
                  ]
print(computer_parts)

#REPLACING AN ITEM FROM THE LIST
computer_parts[3] = "trackpad"
print(computer_parts)

#ITERABLE ITEMS IN A LIST
print(computer_parts[3:])
computer_parts[3:] = "trackpad" #when i mention the item in such a way python considers it as a iterable object and seperates all the characterts in the item and creates it as each list
print(computer_parts)

#A SINGLE ITEM OF A LIST
computer_parts[3:] = ["trackpad"] #By keeping the item in barackets we tell python that it is a one single item.
print(computer_parts)