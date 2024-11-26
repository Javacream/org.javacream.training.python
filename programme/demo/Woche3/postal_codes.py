with open('./programme/demo/Woche3/postal_codes.data', 'rt') as data_file:
    raw_rows = data_file.readlines()

# Daten bereinigen, also \n, falls vorhanden, entfernen
rows = []
for row in raw_rows:
    if row.endswith('\n'):
        row = row[0:len(row) - 1] # Hinweis: Das geht noch eleganter
    rows.append(row)
# Jede Zeile separat nach dem = trennen
postal_codes = {}
for row in rows:
    postal_code_and_city = row.split('=')    
    postal_code = postal_code_and_city[0]
    city= postal_code_and_city[1]
    postal_codes[postal_code] = city
# und als Key=Value-Paar einem Dictionary hinzufügen

print(postal_codes)
# Benutzereingabe: Postleitzahl? -> Stadt

while True:
    code = input('Bitte geben Sie eine Postleitzahl ein: ')
    city = postal_codes.get(code)
    if city != None:
        print(f'Die PLZ {code} steht für {city}')
    else:
        print(f'Die PLZ {code} wurde nicht gefunden')    
    again = input ('Nochmal? j|n: ')
    if (again == 'n'):
        break

