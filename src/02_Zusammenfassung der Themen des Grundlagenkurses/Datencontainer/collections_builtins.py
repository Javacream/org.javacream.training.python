my_list = ['a', 'b', 'c', 'b', 'd', 'a']
print(len(my_list)) # 6
print(my_list[1]) # b
my_set = set(my_list)
print(len(my_set)) # 4
# my_set[1] # Fehler, 'set' object is not subscriptable
my_list = list(my_set)
print(len(my_list)) # 4
print(my_list[1]) # Nicht mehr determiniert, durch das Set ist die ursprüngliche Ordnung nicht mehr vorhanden

if 'b' in my_list:
    print(f'{my_list} contains b')

if not 'f' in my_list:
    print(f'{my_list} does not contain f')