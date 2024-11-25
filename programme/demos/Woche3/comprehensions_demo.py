names = ['Hugo', 'Frieda', 'Andrea', 'Harald', 'Fritz']

# Länge des Namens, wenn Name in Namenslist mit 'H' beginnt

result = [len(name) for name in names if name.startswith('H')]

print(result)