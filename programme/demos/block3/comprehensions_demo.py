names = ['Hugo', 'Frieda', 'Andrea', 'Harald', 'Fritz']

# Länge des Namens, wenn Name in Namenslist mit 'H' beginnt

result = []
for name in names:
    if name.startswith('H'):
        result.append(len(name))

print(result)