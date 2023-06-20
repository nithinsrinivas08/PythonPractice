menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "spam", "spamegg"],
        ]
for meal in menu :
    if "spam" not in meal :
        print(meal)
        for item in meal :
            print(item)
    else :
        print("{0} has spam score of {1}".format(meal, meal.count("spam")))