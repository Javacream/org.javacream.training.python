postal_codes = {'81371': 'München', '30000': 'Berlin', '30001': 'Berlin', '99999': 'Utopia', '99999': 'Nicht belegt'}

print(f'{postal_codes} hat {len(postal_codes)} Elemente')

print(postal_codes['81371'])
print(postal_codes['30000'])

# print(postal_codes['40000']) # KeyError

# Iterieren

print('#################### ')

for postal_code in postal_codes:
    print(f'{postal_code}={postal_codes[postal_code]}')
