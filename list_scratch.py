names = ['Hugo', 'Egon', 'Andrea', 'Hannah']
name_with_index_1 = names[2]
print(name_with_index_1)
for e in names:
    print(e)

names.append('John')

print('Hello')
# append('John')
# names.print('Hello')

sub_names = names[1:3:2]
print(sub_names)

# details

# defaults
sub_names = names[:3] # default start = 0
sub_names = names[1:] # default end = len(names)
sub_names = names[:] # possible, but names.copy() is a better alternative
sub_names = names[::-1] # reverted list
print(sub_names)
print("Hugo"[::-1])