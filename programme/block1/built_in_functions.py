# Funktion ohne runde Klammern führt keine Aktion aus!

name = input
print(name)

# es gibt Funktionen, die keine Werte zurückliefern

age = print("Alter eingeben: ")
print(age)

# NIEMALS EINE VARIABLE WIE EINE BUILT-IN-FUNKTION BENENNEN!
input = input("Bitte nochmal einen Namen eingeben: ")
print(input)

input = input("Und nochmal bitte einen Namen eingeben: ")
print(input)