# Dieses Skript berechnet einen BMI-Wert, siehe Wikipedia

weight = 76.6 # Fließkommazahl mit dem Punkt als Trennzeichen
height = 183 # Ganzzahhl
name = 'Hugo' # Zeichenkette mit beliebiger Länge, eingeschlossen in einfache oder doppelte Hochkommas

height_in_meter = height / 100 # Variablennamen in Python nur Kleinbuchstaben und _ zur Unterteilung
bmi = weight / (height_in_meter * height_in_meter) # weight / (height **2), also ** -> Pozenzieren

print(bmi)