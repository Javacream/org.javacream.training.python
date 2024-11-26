with open('./programme/demo/Woche3/postal_codes.data', 'rt') as data_file:
    raw_rows = data_file.readlines()

rows = [row[:-1] if row.endswith('\n') else row for row in raw_rows ]
postal_codes = {row.split('=')[0]:row.split('=')[1] for row in rows}


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

