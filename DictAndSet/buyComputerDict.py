availableParts = { "1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "table",
                   "6": "hdmi",
                   "7": "dvd drive"}

currentChoice = None
computerParts = {}
 
while currentChoice != "0" :
    if currentChoice in availableParts :
        chosenPart = availableParts[currentChoice]
        if currentChoice in computerParts:
            # it's already in, so remove it
            print(f"Removing {chosenPart}")
            computerParts.pop(currentChoice)
        else:
            print(f"Adding {chosenPart}")
            computerParts[currentChoice] = chosenPart
        print(f"Your list now contains: {computerParts}")
    else :
        print("Please add options from the list")
        for key,value in availableParts.items() :
            print(f"{key}: {value}")
        print("0: to finish")

    currentChoice = input("> ")
