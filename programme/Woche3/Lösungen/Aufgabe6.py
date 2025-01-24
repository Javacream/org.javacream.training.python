data = {'A': 42, 'B': 44, 'C': -1}

# Summe der Werte:
print(sum(data.values()))

# Tupel der Key-Value-Paare: 
print(list(data.items()))

# Prüfe, ob Key vorhanden:
if 'C' in data:
    print(f'C ist in {data} enthalten')
if not 'D' in data:
    print(f'D ist in {data} nicht enthalten')    