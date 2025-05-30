# Öffnen der Datei unter Angabe der Lokation und des Encodings
# Dateiinhalt einer Variaben Zuordnen
# Schließen der Datei

with open('programme/Präsenztag2/people.txt', encoding='utf-8') as people_file:
    content = people_file.readlines()
print(len(content))