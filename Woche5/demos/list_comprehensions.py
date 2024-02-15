# Voraussetzung für den Einsatz
# "Ich benötige eine Liste als Ergebnis"
# "Die Ausgangsdaten sind in einer 'iterierebaren Form' vorhanden" (Set, List, Dictionary, Tuple, Range, Strings, ...)


# Beispiele
# "Sämtliche" Such-Operationen, find_people_by_age, find_people_by..., 
# find_person_by_user_id hat nur einen Treffer, also keine Comprehension nötig

names = ["Hugo", "Fritz", "Emil", "Hugo", "Eduard", "Fridolin"]
r = range(42)

# Suche mir aus der Namens-Liste alle Hugos
hugos = [name for name in names if name == "Hugo"]
print(hugos)

# wie viele Hugos sind in der Liste vorhanden?
number_of_hugos = len([name for name in names if name == "Hugo"])
print(number_of_hugos)

# Lösung ohne Comprehension
print(names.count("Hugo"))

# Bestimme mir die Namen, die mit "F" beginnen!
# Bestimme mir die Namen, aus vier Buchstaben bestehen
# Bestimme mir die Länge der Liste
# Füge den Namen "Hannah" der Liste hinzu
#...


