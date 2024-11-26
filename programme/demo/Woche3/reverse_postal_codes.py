with open('./programme/demo/Woche3/postal_codes.data', 'rt') as data_file:
    raw_rows = data_file.readlines()

# Daten bereinigen, also \n, falls vorhanden, entfernen
rows = []
for row in raw_rows:
    if row.endswith('\n'):
        row = row[0:len(row) - 1] # Hinweis: Das geht noch eleganter
    rows.append(row)
# Jede Zeile separat nach dem = trennen
reverse_postal_codes = {}
for row in rows:
    postal_code_and_city = row.split('=')    
    postal_code = postal_code_and_city[0]
    city= postal_code_and_city[1]
    postal_codes = reverse_postal_codes.get(city)
    if postal_codes == None:
        postal_codes = []
        reverse_postal_codes[city] = postal_codes
    postal_codes.append(postal_code)
while True:
    city = input('Bitte geben Sie eine Stadt ein: ')
    codes = reverse_postal_codes.get(city)
    if codes != None:
        print(f'Die PLZs für {city} sind: {codes}')
    else:
        print(f'Die PLZs für {city} wurden nicht gefunden')    
    again = input ('Nochmal? j|n: ')
    if (again == 'n'):
        break

