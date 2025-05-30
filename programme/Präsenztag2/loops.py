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