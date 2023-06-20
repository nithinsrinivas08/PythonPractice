albums = [("Welcome to my nightmare", "Alice Cooper", 1975,
           [(1, "Welcome to my nightmare"),
            (2, "Devil's food"),
            (3, "The Black widow"),
            (4, "Samo Folks"),
            (5, "Only Women Bleed")
           ]
          ),
          ("Bad Comapny", "Bad Company", 1974,
           [(1, "Cant get enough"),
            (2, "Rock Steady"),
            (3, "Ready For Love"),
            (4, "Doint let me down"),
            (5, "Bad Company"),
            (6, "The way i choose"),
            (7, "Movin on"),
            (8, "Swagull")
           ]
          ),
         ]
for name,artist,year,songs in albums :
    print("Albumn : {}, {}, {}, {}".format(name,artist,year,songs))

ready = albums[1][3][2][1] #TO RETRIEVE READY FOR LOVE FROM THE ABOVE LIST
print(ready)

badCompany = albums[1][3][5][1]
print(badCompany)

