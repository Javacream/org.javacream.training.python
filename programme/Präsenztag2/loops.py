r = range(1, 5)
for i in r:
    print(i)

r = range(1, 5, 2)
for i in r:
    print(i)

candidate = 3
if candidate in r:
    print(f'{candidate} ist in {r} enthalten')
else:
    print(f'{candidate} ist in {r} nicht enthalten')

names = ['A', 'B', 'C']
for name in names:
    print(name)


candidate = 'D'
if candidate in names:
    print(f'{candidate} ist in {names} enthalten')
else:
    print(f'{candidate} ist in {names} nicht enthalten')

print(f'Länge von names: {len(names)}')
print(f'Erstes Element von names: {names[1]}')