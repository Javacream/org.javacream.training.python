names = {'Eduard', 'Hugo', 'Emil'}

result = []
for name in names:
    if name.startswith('E'):
        result.append(name)

result = [letter for name in names for letter in name if name.startswith('H')]
print(result)