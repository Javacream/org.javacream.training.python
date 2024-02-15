# Sortiert werden können alle Datencontainer, die eine innere Ordnung aufweisen

names = ["Hugo", "Fritz", "Emil", "Hugo", "Eduard", "Fridolin", "Edgar"]
names.sort()
names.sort(reverse = True)
print(names)

# Sortieren nach anderen Algorithmen, als dem "natürlichen" Algorithmus

# Anderer Algorithmus: Sortiere nach der Länge einer Zeichenkette

# Schritt 1: Schreibe einen Algorithmus, der aus einer Zeichenkette seine Länge bestimmt

def string_len(text):
    return len(text)

# Schritt 2: Übergebe diesen Algorithmus als key in der sort-Funktion

# names.sort(key=string_len()) # so nicht: Hier wird die Funktion versucht aufzurufen -> QUATSCH
names.sort(key=string_len)
#print(names)
names.sort(reverse= True, key=string_len)
#print(names)

# NEU und nicht unbedingt notwendig
# Lambda-Ausdrücke in Python

string_len_lambda = lambda text: len(text)
names.sort(key=string_len_lambda)
# print(names)

# Weitere, finale Verkürzung
names.sort(key=lambda name: len(name))
print(names)

 



