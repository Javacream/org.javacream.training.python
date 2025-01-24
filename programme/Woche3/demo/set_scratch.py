# set = {'A', 'B', 'C'} -> bitte niemals eine Variable namens set benutzten, set ist nämlich eine BuiltIn-Funktion

my_set = {'A', 'B', 'C'}
print(len(my_set))
# print(my_set[1])

my_set = {'A', 'B', 'C', 'A', 'D'} # Werte können mehrfach hinzugefügt werden, Duplikate werden erkannt
print(len(my_set))
# print(my_set[1])

for element in my_set:
    print(element)


