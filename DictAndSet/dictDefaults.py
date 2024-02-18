from contents import pantry

chickenQuantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chickenQuantity}")

beansQuantity = pantry.setdefault("beans", 0)
print(f"beans : {beansQuantity}")

ketchupQuantity = pantry.get("ketchup", 0)
print(f"ketchup : {ketchupQuantity}")

print()
print("The items in the pantry....")
for key, value in sorted(pantry.items()):
    print(key, value)
