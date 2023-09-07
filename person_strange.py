def use_vars():
    person1_lastname = "Sawitzki"
    person1_firstname = "Rainer"
    person1_height = 183
    person1_weight = 81

    person2_lastname = "Mustermann"
    person2_firstname = "Andrea"
    person2_height = 176
    person2_weight = 66

def use_dict():
    person1 = {"lastname": "Sawitzki", "firstname": "Rainer", "height": 183, "weight": 81}
    person2 = {"lastname": "Mustermann", "firstname": "Andrea", "height": 176, "weight": 66}

    # Ausgabe des Nachnamens von Person 1

    print(person1.get("sdfghjkljhgf")) # KEINE FEHLERMELDUNG IN VSC

def scratch():
    people = []
    while(True):
        lastname = input("Enter lastname:") # besser: Einlesen einer Datei
        # ...
        new_person = {"lastname": lastname}
        people.append(new_person)


use_dict()