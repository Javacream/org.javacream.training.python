seasons = ('spring', 'summer', 'automn', 'winter')
print(type(seasons))

todos = ['spring', 'summer', 'automn', 'winter']
print(type(todos))

todos_set = {'spring', 'summer', 'automn', 'winter'}
print(type(todos_set))

r = range(0, 5)
print(type(r))

postal_codes = {'81371': 'München', '70567': 'Stuttgart', 1: 'Hugo'}
print(type(postal_codes))


for element in postal_codes:
    print(element)

print(postal_codes[1])    
# print(seasons[4])

characters = ['A', 'B', 'A', 'D']
unique_characters = set(characters)
print(unique_characters)

print(len(characters))
print(len(unique_characters))

name = 'Sawitzki'
print(name[4])
print(len(name))
for char in name:
    print(char)

name_as_list = list(name)
print(name_as_list)
name_as_set = set(name)
print(name_as_set)
