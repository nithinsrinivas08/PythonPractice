menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "spam", "spamegg"],
        ]

for meal in menu :
    for i in range(len(meal) -1, -1, -1) :
        if meal[i] == "spam" :
            del meal[i]
    print(", ".join(meal)) 