names_list = ['Hugo', 'Emil', 'Fritz', 'Hugo', 'Hannah']

# Ohne Comprehension
result_list = [] # Erzeuge eine initial leere Ergebnisliste
for name in names_list: # Iteriere über die Eingangsdaten
	extended_name = f'Hello {name}!'
	result_list.append(extended_name)
#print(result_list)


# Mit List Comprehension

result_list = [f'Hello {name}!' for name in names_list ]
#print(result_list)


# Ohne Comprehension
result_list = [] # Erzeuge eine initial leere Ergebnisliste
for name in names_list: # Iteriere über die Eingangsdaten
    if name == 'Hugo':
        extended_name = f'Hello {name}!'
        result_list.append(extended_name)
print(result_list)

# Mit List Comprehension

result_list = [f'Hello {name}!' for name in names_list if name == 'Hugo']
print(result_list)
