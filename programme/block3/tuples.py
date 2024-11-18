names_tuple = tuple(['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah'])

names_list = list(names_tuple)
names_tuple = tuple(names_list)
n = 2
print(f'das {n}-te Element des Tuples {names_tuple} ist {names_tuple[n]}')
name = 'Hugo'
print(names_tuple.count(name) > 0)
