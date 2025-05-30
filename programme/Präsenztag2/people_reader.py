# Öffnen der Datei unter Angabe der Lokation und des Encodings
# Dateiinhalt einer Variaben Zuordnen
# Schließen der Datei

people_file = open('programme/Präsenztag2/people.txt', encoding='utf-8')
content = people_file.readlines()
people_file.close()