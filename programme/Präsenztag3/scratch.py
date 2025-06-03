my_list = ['A', 'B', 'C']

person_info = ['Sawitzki', 183, 76.6, True]


print(len(my_list))
print(len(person_info))

print(person_info[1])

i = 0
while i < len(my_list):
    element_at_i = my_list[i]
    print(element_at_i)
    i = i + 1

for element in my_list:
    print(element)


my_list[0] = 'Hugo'
new_name = 'Emil'
my_list[1] = new_name

# my_list[3] = 'Rainer'

my_list.append('Rainer')
my_list.insert(1, 'Hannah')
print(my_list)


