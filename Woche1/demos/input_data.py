name = input("Bitte Name eingeben: ")
weight = input ("Bitte Gewicht eingeben: ")
print(type(weight))
print(name + " wiegt " + weight + " Kilo")

# weight = weight + 1.1 # FEHLER: 1.1 ist eine Kommazahl, weight ist aktuell ein String!
weight = float(weight) # Python versucht nun, die Zeichenkette als Zahl zu interpretieren -> Kann auch fehlschlagen, -> Morgen
weight = weight + 1.1
print(name + " wiegt nun " + str(weight) + " Kilo")


