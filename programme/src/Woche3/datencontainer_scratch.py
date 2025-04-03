# Startsituation
lastname = "Sawitzki"
firstname = "Rainer"
weight = 76.5
height=183
name = "Neptun 3"

# Gruppieren von Informationen, z.B. in einer List

person = ["Sawitzki", "Rainer", 76.5]
boat = ["Neptun 3", 183]


# Mit Dictionary

person_dict = {"lastname": "Sawitzki", "firstname": "Rainer", "weight": 76.5}
boat_dict = {"name": "Neptun 3", "height": 183}

# Keys können "alles" sein
person_dict = {0: "Sawitzki", "Eins": "Rainer", True: 76.5}

# Aggregat von Collections  
people = [
    {"lastname": "Sawitzki", "firstnames": ["Rainer", "Ulrich"], "weight": 76.5},
    {"lastname": "Sawitzki", "firstname": "Klaus", "weight": 76.5},
    {"lastname": "Schneider", "firstname": "Hannah", "weight": 76.5}
    ]


print("done")
