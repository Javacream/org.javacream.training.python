# Nach eingabe eines Namens und eines Gewichts und der Körpergröße wird der Body Mass Index berechnet

MIN_WEIGHT = 0.5
MAX_WEIGHT = 333
MIN_HEIGHT = 0.25
MAX_HEIGHT = 2.5

name = input("Bitte Namen eingeben: ")
weight = input (f"Bitte Körpergewicht in kg zwischen {MIN_WEIGHT} und {MAX_WEIGHT} eingeben: ")
height = input (f"Bitte Körpergröße in m zwischen 0.25 und 2.5 eingeben: ")
try:
    weight = float(weight)
    height = float(height)
    valid = False
    if weight >= MIN_WEIGHT and weight <= MAX_WEIGHT:
        if height >= MIN_HEIGHT and height <= MAX_HEIGHT:
            bmi = weight / ( height * height ) 
            valid = True
    if valid:
        print(f"Name: {name} mit Gewicht: {weight} und Größe {height} hat einen BMI von {bmi}") # Format-String
    else:
        print(f"Ungültiger Bereich für Gewicht oder Körpergröße: {weight}, {height}")    

except:
    print(f"Fehler, Gewicht {weight} oder Größe {height} können  nicht als Zahl interpretiert werden")

print("Fertig")