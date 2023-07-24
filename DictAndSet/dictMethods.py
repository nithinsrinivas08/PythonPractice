d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv" : "four"
}

pantryItems = ['chicken', 'spam', 'egg', 'bread', 'lemon']
#newDict = dict.fromkeys(pantryItems,0)
#print(newDict)

#KEYS METHOD
#keys = d.keys()
#print(keys)

#UPDATE METHOD
'''d2 = {
    7:"lucky seven",
    8:"ten",
    9:"this is the new three"
}
d.update(d2)
for key,value in d.items():
    print(key,value)'''

#VALUES METHOD
v = d.values()
print(v)
print("four" in v)
print("eleven" in v)
keys = list(d.keys())
values = list(v)
if "four" in values :
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")
#the same thing as above but it does not store the whole dictionary again
print()
for key, value in d.items():
    if value=="four" :
        print(f"{d[key]} was found with the key {key}")