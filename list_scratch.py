numbers = [1,3,42,-9,5]
names = ['Hugo', 'Andrea', 'Helga']
mixed = ['Hugo', 76.6, 1.83]
nested = [
    [['Hugo', 'Franz'], 76.6, 1.83],
    ['Andrea', 66.6, 1.66],
    ['Helga', 86.6, 1.93]
]

person1 = ['Hugo', 'Sawitzki']
person2 = ['Andrea', 'Meier']
person3 = ['Helga', 'Müller']
people = [person1, person2, person3]
numbers_length = len(numbers)
print(f'{numbers} hat {numbers_length} Elemente')
print(f'{numbers} hat {len(numbers)} Elemente')

print(numbers[2])
print(numbers[0])
#print(numbers[10]) # index out of range
print(numbers[-1]) # Letzte Element, äquivalent zu numbers[len(numbers)-1]
print(numbers[-3])
#print(numbers[-10]) # index out of range

print(nested[0])

sub_list = nested[0]
print(sub_list[1])

print(nested[0][1])

# print(nested[0, 1]) Funktioniert nicht

print(nested[0][0][1])
