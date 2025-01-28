names = ['Emil', 'Harald', 'Andrea', 'Helga']

# Filtere mir alle Einträge, die mit 'H' beginnen

# Klassisch, mit ausgeschriebener Schleife und Filterung
result = []
for name in names:
    if name.startswith('H'):
        result.append(name)
print(result) 

# List Comprehension mit Filterung
result = [name for name in names if name.startswith('H')]
print(result) 

# Klassisch, mit ausgeschriebener Schleife und Transformation
result = []
for name in names:
    result.append(len(name))
print(result) 

# List Comprehension mit Transformation
result = [len(name) for name in names]
print(result) 

# Klassisch, mit ausgeschriebener Schleife und Filterung und Transformation
result = []
for name in names:
    if name.startswith('H'):
        result.append(len(name))
print(result) 

# List Comprehension mit Filterung und Transformation
result = [len(name) for name in names if name.startswith('H')]
print(result) 
