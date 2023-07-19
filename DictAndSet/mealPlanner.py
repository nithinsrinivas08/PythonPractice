from contents import pantry, recipes

def addShoppingItem(data :dict, item: str, amount:int) -> None:
    '''if item in data:
       data[item] += amount
    else :
        data[item] = amount'''
    data[item] = data.setdefault(item,0) + amount

displayDict = {}

for index, key in enumerate(recipes):
    #print(index,key)
    displayDict[str(index+1)] = key

shoppingList = {}

while True :
    print("Please choose your recipe")
    print("-------------------------")

    for key,value in displayDict.items():
        print(f"{key} - {value}")
    choice = input(": ")

    if choice == "0":
        break
    elif choice in displayDict :
        selectedItem = displayDict[choice]
        print(f"You have selected {selectedItem}")
        print("checking ingredients ....")
        ingredients = recipes[selectedItem]
        print(ingredients)

        for foodItem,requiredQuantity in ingredients.items() :
            quantityInPantry = pantry.get(foodItem, 0)

            if requiredQuantity <= quantityInPantry :
                print(f"\t{foodItem} OK")
            else :
                quantityToBuy = requiredQuantity - quantityInPantry
                print(f"\tYou need to buy {quantityToBuy} of {foodItem}")
                addShoppingItem(shoppingList,foodItem,quantityToBuy)

for things in shoppingList.items():
    print(things)