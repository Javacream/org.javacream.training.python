postal_codes = {'81373': 'München', '70567': 'Stuttgart'}

print(postal_codes)

print(postal_codes['81373'])

print(len(postal_codes))

for key in postal_codes:
    print(f'{key} = {postal_codes[key]}')


# Nachbildung eines dicts, nicht ernst gemein...

key1 = '81372'
key2 = '70567'
value1 = 'München'
value2 = 'Stuttgart'

selection = '81372'
if selection == key1:
    result = value1
elif selection == key2:
    result = value2
else:
    result = "Not found"    