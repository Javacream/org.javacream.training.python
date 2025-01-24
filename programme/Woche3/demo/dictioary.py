plz = input("Bitte PLZ eingeben: ")
postal_codes = dict()
postal_codes["81371"] = "München"
postal_codes["73567"] = "Stuttgart"
postal_codes["30000"] = "Berlin"

#city = postal_codes[plz]
city = postal_codes.get(plz, 'Unknown')
print(city)           
city = postal_codes["40000"] = "Hamburg"
print(city)           
