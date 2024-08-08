prompt = 'Bitte Namen eingeben: '
name = input(prompt)
# Variante 1
out = 'Sie haben den Namen ' + name + 'eingeben'
print(out)
# Variante 2
print ('Sie haben den Namen ', name, ' eingegeben!')

# Variante 3: Formatted String
print(f'Sie haben den Namen {name} eingegeben!')