from recipesChallenge import myDeep
import copy

original = {
    "Nit": ["Sri", ["Programmer", "Teacher"]],
    "hin": ["nivas", ["Programmer", "Teacher"]]
}

copy1 = copy.deepcopy(original)
copy2 = myDeep(original)

original["Nit"].append("Space")
original["hin"].append("Maths")

original["Nit"][1].append("BA")
secList = original["hin"]
secList[1].append("BI")
print(original)
print(copy1)
print(copy2)
print(secList)