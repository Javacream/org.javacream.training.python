# Nach eingabe eines Namens und eines Gewichts wird der Body Mass index berechnet

number1 = 4
number2 = 8

# Mathematische Berechnungen
result = number1 + number2
result = number1 - number2
result = number1 * number2
result = number1 / number2

name = input("Bitte Namen eingeben: ")
weight = input ("Bitte Körpergewicht eingeben: ")
# weight = weight / name 
weight = float(weight)
weight = 2 * weight
#print("Name: " + name + ", Gewicht: " + weight)# Laufzeitfehler
#print("Name: " + name + ", Gewicht: " + str(weight)) # funktioniert, ist aber nicht sonderlich schön
print(f"Name: {name}, Gewicht: {weight}") # Format-String