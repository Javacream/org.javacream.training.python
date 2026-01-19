postalcodes = {'80000': 'München', '76543': 'Stuttgart', '30333': 'Bremen', '10128': 'Berlin'}

print(postalcodes['80000'])
#print(postalcodes['80001']) # KeyError
print(postalcodes.get('80001', 'unknown'))
for key in postalcodes:
    print(f'{key} = {postalcodes[key]}')

for key, value in postalcodes.items():
    print(f'{key} = {value}')

postalcodes['40111'] = 'Düsseldorf'
postalcodes['30333'] = 'Hamburg'
postalcodes['80123'] = 'München'

print(postalcodes)


city_to_postalcodes = {'München': ['80000', '80123'], 'Stuttgart': ['76543']}
print('done')
