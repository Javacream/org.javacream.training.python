# Nach eingabe eines Namens und eines Gewichts wird der Body Mass index berechnet


name = input("Bitte Namen eingeben: ")
weight = input ("Bitte Körpergewicht in kg eingeben: ")
height = input ("Bitte Körpergröße in m eingeben: ")
try:
    weight = float(weight)
    height = float(height)
    bmi = weight / ( height * height ) 
    print(f"Name: {name} mit Gewicht: {weight} und Größe {height} hat einen BMI von {bmi}") # Format-String
except:
    print(f"Fehler, Gewicht {weight} oder Größe {height} können  nicht als Zahl interpretiert werden")

print("Fertig")