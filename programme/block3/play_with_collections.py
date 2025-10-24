# ohne Dictionary

collection = ['Hugo', 'Emil', 'Hannah', 'Hugo']
collection = ('Hugo', 'Emil', 'Hannah', 'Hugo')
collection = {'Hugo', 'Emil', 'Hannah', 'Hugo'}
collection = 'Hello Hannah!'

print(len(collection))

for element in collection:
    print(element)

candidate = 'Hannah'

if candidate in collection:
    print(f'{candidate} is in {collection}')
else:
    print(f'{candidate} is not in {collection}')

print(collection[1])    

# Range, z.B. Iteriere von 1-4, 1-8 step3, Rückwärts?