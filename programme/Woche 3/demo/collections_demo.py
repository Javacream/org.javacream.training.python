names_list = list(['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah']) # eine Liste mit den angegebenen Elementen
names_tuple = tuple(['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah']) # ein Tupel mit den angegebenen Elementen
names_set = set(['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah']) # ein Set mit den angegebenen Elementen
name_address_dict = dict(Emil= 'Berlin', Fritz= 'München', Hugo= 'Berlin', Hannah= 'Düsseldorf') # ein Dictionary mit den angegebenen Key-Value-Paaren
from_1_to_9 = range(1, 10)
from_1_to_9_step_4 = range(1, 10, 4)


second_name_in_list = names_list[1]
second_name_in_tuple = names_tuple[1]
#second_name_in_set = names_set[1], ein Set hat keinen Zugriff auf ein einzelnes Element!
address_of_hannah = name_address_dict['Hannah']

# Fehlerhafte Zugriffe
#sixth_name_in_list = names_list[5]
#sixth_name_in_tuple = names_tuple[5]
#address_of_andrea = name_address_dict['Andrea']

# Skurriler Zugriff
minus_one_name_in_list = names_list[-1]

# Iteration
for element in from_1_to_9_step_4:
    print(element)

for key in name_address_dict:
    print(key, name_address_dict[key])

# Dynamik der Collections
# Ersetzen von Elementen
names_list[1] = 'Eduardo'
#names_tuple[1] = 'Eduardo' unveränderlich
#names_set[1] = 'Eduardo' kein Index
name_address_dict['Emil'] = 'Mannheim'

# Hinzufügen von Elementen
#names_list[5] = 'Helga' diese Art des Zugriffs funktioniert nur bei vorhandenen Indizes
#names_tuple[1] = 'Eduardo' unveränderlich
#names_set[1] = 'Eduardo' kein Index
name_address_dict['Helga'] = 'Heidelberg'

# Bestimmen der Länge einer Collection
length_of_collection = len(name_address_dict)
print(length_of_collection)

names_list.sort()
names_set.clear()
print ('Done')

