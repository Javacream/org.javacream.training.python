""" names = ['Hugo', 'Frieda', 'Andrea', 'Hugo', 'Fritz']
for name in names:
    print(name)
print(names[-2])
sub_names_list = names[2:]
print(sub_names_list)    
print(len(names))
print(len(sub_names_list))

text = "Ein Text"
for character in text:
    print(character)
print(text[2])    
 """

names = {'Hugo', 'Frieda', 'Andrea', 'Hugo', 'Fritz'}
for name in names:
    print(name)

element = 'Andreas'
if element in names:
    print(f'{element} ist in der Names-Collection')
else:
    print(f'{element} ist nicht in der Names-Collection')
