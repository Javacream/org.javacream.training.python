# file = open ('./data.txt') # der optionale 2. Parameter ist 'rt', Lesen einer Text-Datei
with open ('./data.txt', 'rt') as file:
    rows = file.readlines()
print(rows)