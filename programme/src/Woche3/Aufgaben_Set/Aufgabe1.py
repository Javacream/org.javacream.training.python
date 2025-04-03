set1 = ('A', 'B', 'C', 'K', 'L')
set2 = ('C', 'L', 'E')

for element in set1:
    if element in set2:
        print(f'{element} ist im Schnitt von set1 und set2 enthalten')

for element in set1:
    if not element in set2:
        print(f'{element} ist Bestandteil der Vereinigung von set1 und set2')
for element in set2:
    print(f'{element} ist Bestandteil der Vereinigung von set1 und set2')
        