names_list = ['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah'] # eine Liste mit den angegebenen Elementen
names_tuple = ('Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah') # ein Tupel mit den angegebenen Elementen
names_set = {'Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah'} # ein Set mit den angegebenen Elementen
name_address_dict = {'Hugo': 'München', 'Emil': 'Berlin', 'Fritz': 'München', 'Hugo': 'Berlin', 'Hannah': 'Düsseldorf'} # ein Dictionary mit den angegebenen Key-Value-Paaren


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
for element in names_set:
    print(element)

for key in name_address_dict:
    print(key, name_address_dict[key])


print ('Done')

