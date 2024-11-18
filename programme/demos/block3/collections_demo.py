# names = ['Hugo', 'Frieda', 'Andrea', 'Hugo', 'Fritz']
# for name in names:
#     print(name)
# print(names[-2])
# sub_names_list = names[2:]
# print(sub_names_list)    
# print(len(names))
# print(len(sub_names_list))

# text = "Ein Text"
# for character in text:
#     print(character)
# print(text[2])    

# names = {'Hugo', 'Frieda', 'Andrea', 'Hugo', 'Fritz'}
# for name in names:
#     print(name)

# element = 'Andreas'
# if element in names:
#     print(f'{element} ist in der Names-Collection')
# else:
#     print(f'{element} ist nicht in der Names-Collection')


# names_list = ['Hugo', 'Frieda', 'Andrea', 'Hugo', 'Fritz']
# # names_set = {'Hugo', 'Frieda', 'Andrea', 'Hugo', 'Fritz'}

# names_set = set(names_list)
# print(type(names_list))
# print(type(names_set))
# names_list = list(names_set)
# print(names_list)

# eduard_list = list("Eduard")
# print(eduard_list)

# numbers = [3, -7, 8, 42, 1]
# print(sum(numbers), min(numbers), max(numbers))

r1 = range(0, 5)
for number in r1:
    print(number)

r2 = range(0, 5, 2)
for number in r2:
    print(number)    

r3 = range(0, -5, -1)
for number in r3:
    print(number)    

# r4 = range(0, 5, 1.2) # Fehler: ranges nur mit Ganzzahlen
# for number in r4:
#     print(number)    

print(r1[2])
numbers_list = list(r1)
print(numbers_list)
r4 = range(numbers_list)