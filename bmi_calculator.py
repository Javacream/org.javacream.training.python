# Nach eingabe eines Namens und eines Gewichts wird der Body Mass index berechnet


name = input("Bitte Namen eingeben: ")
weight = input ("Bitte Körpergewicht eingeben als Zahl: ")
try:
    weight = float(weight)
    weight = 2 * weight
    print(f"Name: {name}, Gewicht: {weight}") # Format-String
except:
    print(f"Fehler, das eingegebene Gewicht {weight} kann nicht als Zahl interpretiert werden")

print("Fertig")