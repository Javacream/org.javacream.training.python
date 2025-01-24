# list = ['A', 'B', 'C'] -> bitte niemals eine Variable namens list benutzten, list ist nämlich eine BuiltIn-Funktion

my_list = ['A', 'B', 'C']
print(len(my_list))
print(my_list[1])

my_list = ['A', 'B', 'C', 'A', 'D'] # Werte können mehrfach hinzugefügt werden
print(len(my_list))
print(my_list[1])

for element in my_list:
    print(element)


