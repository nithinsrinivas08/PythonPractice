lionList = ["scary","big","cat"]
elephantList = ["big","grey","wrinkled"]
teddyList = ["cuddly","stuffed"]
animals = {
    "lion" : lionList,
    "elephant" : elephantList,
    "teddy" : teddyList,
}

#things = animals.copy()
things = {
    "lion" : lionList,
    "elephant" : elephantList,
    "teddy" : teddyList,
}
print(things["teddy"])
print(animals["teddy"])
print()
#things["teddy"].append("toy")
teddyList.append("toy")
animals["teddy"].append("added through animals")
things["teddy"].append("added through things")
print(things["teddy"])
print(animals["teddy"])