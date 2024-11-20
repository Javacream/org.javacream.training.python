# Demonstration der Wiederholungslogik in Python

counter = 0
MAX = 5

#print(counter < MAX)

# Endlosschleife, Abbrechen mit STRG-C oder gleich das Terminal-Fenster wegwerfen
#while (counter < MAX):
#     print("counter kleiner MAX") 

while (counter < MAX):
    print(f"{counter} kleiner {MAX}") 
    counter = counter + 3


elements = ["Bohne", "Erbse", "Tomate"] # geordnete Liste mit Elementen

# elements2 = ("Bohne", "Erbse", "Tomate") # Ein Tupel, ein unveränderliche List -> List, Array, Tuple, Range, Dictionary -> Woche 3

# Iteration = Wiederholung für alle Elemente der Liste

# for-in-Schleife
for element in elements:
    print(f"{element}")

# for (counter = 0; counter < MAX; counter = counter + 1): # Klassische for-Schleife wird in Python nicht unterstützt
#    print(f"{counter} kleiner {MAX}") 
# for 1 to 10: # nicht unterstützt
#    print(index) 
       