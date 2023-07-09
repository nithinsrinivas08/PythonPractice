vehicles = {
    'dream' : 'Honda 250T',
    'roadster' : 'BMW R1100',
    'er5' : 'Kawasaki ER5',
    'can-am' : 'Bombardier Can-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha XT650',
    'jimny' : 'Suzuki Jimny 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4',
}

myCar = vehicles['fiesta'] #as we use square brackets then it refers to indexing
print(myCar)

learner = vehicles.get("er5") #here instead of indexing we use the GET method
print(learner)

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"
vehicles["virago"] = "Yamaha XV535"
del vehicles['toy'] 
#del vehicles["f1"]
result = vehicles.pop("f1", None)
print(result)

for key in vehicles :
    print(key, vehicles[key], sep=" : ")