n = int(input('Bitte Ganzzahl eingeben: '))
interval = range(1, n+1)

squared_numbers = dict()
for number in interval:
    squared_numbers[number] = number*number


for key in squared_numbers:
    print(key)


key_list = ['Hugo', 'Emil']
value_list = ['Berlin', 'Hannover']

name_address_dict = dict()
index = 0
for key in key_list:
    name_address_dict[key] = value_list[index]
    index += 1

print(name_address_dict)

print(sum(squared_numbers.values()))


# Dictionary in Tuple, Variante 1

name_address_tuple_list = list() # []
for name in name_address_dict:
    name_address_tuple = (name, name_address_dict[name])
    name_address_tuple_list.append(name_address_tuple)
print(name_address_tuple_list)


# Dictionary in Tuple, Variante 2

name_address_tuple_list = name_address_dict.items()
print(list(name_address_tuple_list))


# Dictionary in Tuple, Variante 3

name_address_tuple_list = [(name, name_address_dict[name]) for name in name_address_dict]
print(name_address_tuple_list)
