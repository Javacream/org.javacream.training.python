p1 = {'name': 'Sawitzki', 'height': 183}
p2 = {'name': 'Musterperson', 'height': 176}
print(type(p1))
print(f'Der Name von p1 ist {p1['name']}')
print(f'Die Größe von p2 ist {p2['height']}')
# print(p1['weight']) # KeyError: weight ist kein bekannter Schlüssel
p1['height'] = 181
print(f'Die Größe von p1 ist {p1['height']}')
print('done')