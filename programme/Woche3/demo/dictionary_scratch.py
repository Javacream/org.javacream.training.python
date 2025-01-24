# dict = {} -> bitte niemals eine Variable namens dict benutzten, dict ist nämlich eine BuiltIn-Funktion

my_dict = {'A': 42, 'B': 9, 'C': 4711}
print(len(my_dict))
#print(my_dict[1])
print(my_dict['A'])
my_dict = {'A': 42, 'B': 9, 'C': 4711, 'A': 1, 'D': 666} # Key-Value-Paare können mehrfach hinzugefügt werden, doppelte Keys werden erkannt
print(len(my_dict))
# print(my_dict[1])
print(my_dict['A'])

for element in my_dict:
    print(f'{element} -> {my_dict[element]}')


