# ohne Dictionary

collection = ['Hugo', 'Emil', 'Hannah', 'Hugo']

print(len(collection))

for element in collection:
    print(element)

candidate = 'Hannah'

if candidate in collection:
    print(f'{candidate} is in {collection}')
else:
    print(f'{candidate} is not in {collection}')

print(collection[1])    