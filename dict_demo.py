p1 = {'name': 'Sawitzki', 'height': 183}
p2 = {'name': 'Musterperson', 'height': 176}
print(type(p1))
print(f"Der Name von p1 ist {p1['name']}")
print(f"Die Größe von p2 ist {p2['height']}")
# print(p1['weight']) # KeyError: weight ist kein bekannter Schlüssel
p1['height'] = 181
print(f"Die Größe von p1 ist {p1['height']}")
print(len(p1))
for key in p1:
    print(f"{key} = {p1[key]}")

print('done')