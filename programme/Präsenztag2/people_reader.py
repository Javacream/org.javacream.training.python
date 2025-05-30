# Öffnen der Datei unter Angabe der Lokation und des Encodings
# Dateiinhalt einer Variaben Zuordnen
# Schließen der Datei

with open('programme/Präsenztag2/people.txt', encoding='utf-8') as people_file:
    content = people_file.readlines()
# print(len(content))
for row in content:
    row_length = len(row)
    if row[row_length -1] == '\n':
        row = row[0:row_length -1]
    print(row)
    name = row[0:20]
    weight = row[21:26]
    height = row[27:31]
    print(f'{name} {weight} {height}')
