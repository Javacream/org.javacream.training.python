seasons = 'winter', 'spring', 'summer', 'autum'
print(seasons)
for season in seasons:
    print(season)

todos = ['eat', 'sleep']
print(todos)
for todo in todos:
    print(todo)

interval = range(0,3)
for number in interval:
    print(number)
fruits = {'banana', 'apple', 'orange', 'apple'}
for fruit in fruits:
    print(fruit)

postal_codes = {'81373': 'München', '70567': 'Stuttgart'}

for code in postal_codes:
    print(code)

name = 'Hugo'
for character in name:
    print(character)    
# Teilnehmenden-Frage

for code in postal_codes:
    print(f'{code}={postal_codes[code]}')
