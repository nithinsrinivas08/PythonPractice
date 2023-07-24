from contents import recipes

def myDeep(d: dict) -> dict :
    newDict = {}
    for key, value in d.items() :
        newValue = value.copy()
        newDict[key] = newValue
    return newDict

recipeCopy = myDeep(recipes)
recipeCopy["Butter chicken"]["ginger"] = 300
print(recipeCopy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])