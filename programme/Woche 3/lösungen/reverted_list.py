names_list = ['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah']

for name in names_list:
    print(name)

len_names_list = len(names_list)

counter = len_names_list - 1

while counter >= 0:
    print(names_list[counter])
    counter -= 1

counter = -1

while counter > -len_names_list:
    print(names_list[counter])
    counter -= 1
