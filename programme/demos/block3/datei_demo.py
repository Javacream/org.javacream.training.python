# file = open ('./data.txt') # der optionale 2. Parameter ist 'rt', Lesen einer Text-Datei
file = open ('./data.txt', 'rt')
rows = file.readlines()
file.close() # Falls dieser Aufruf nicht gemacht wird, bleibt die Datei bis zum Ende des Python-Prozesses geöffnet und gegegenenfalls gesperrt
print(rows)