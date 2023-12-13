names = ['Hugo', 'Andrea', "Walther", "Emil"]

names.sort()
print(names)
names.sort(reverse=True)
print(names)

# Sortieren nach der Länge der Namen:
names.sort(key = lambda name: len(name))
print(names)

# Sortieren nach dem zweiten Buchstaben des Namen:
names.sort(key = lambda name: name[1])
print(names)

# ...
