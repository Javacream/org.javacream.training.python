with open('people.txt', 'rt', encoding='utf-8') as people_file: 
    lines =  people_file.readlines()
for line in lines:
    # ToDo: Prüfe, ob das letzte Zeichen \n ist und falls ja: Entferne dieses Zeichen
#    if line[-1] == '\n':
#        line = line[:-1]
    line = line.replace('\n', '')    
    # ToDo: Zerlege die line nach dem Strichpunkt
    splitted = line.split(';')
    # ToDo: Zuweisen der einzelnen Teile zu den Personen-Daten
    name = splitted[0]
    weight = float(splitted[2])
    height = float(splitted[3])
    print(f'Gelesene Person: name={name}, Gewicht={weight}, Größe={height}')