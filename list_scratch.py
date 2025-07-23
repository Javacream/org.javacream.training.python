names = ['Hugo', 'Egon', 'Andrea', 'Hannah']
name_with_index_1 = names[2]
print(name_with_index_1)
for e in names:
    print(e)

# alternative iteration
number_of_elements = len(names)
counter = 0
while counter < number_of_elements:
    print(names[counter])
    counter = counter + 1