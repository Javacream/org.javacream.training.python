with open('postal_codes_cities.txt', 'rt') as file:
    content = file.read()
postal_codes_to_cities = eval(content)
with open('city_to_postal_codes.txt', 'rt') as file:
    content = file.read()
city_to_postal_codes  = eval(content)

while True:
    option = input ('PLZ, Ort, Ende? ')
    if option == 'Ende':
        break
    elif option == 'PLZ':
        postal_code = input ('Bitte eine gültige PLZ eingeben: ')
        print(f'Der Ort für die PLZ {postal_code} ist {postal_codes_to_cities[postal_code]}')
    elif option == 'Ort':
        city = input ('Bitte eine gültige Stadt eingeben: ')
        print(f'Die PLZs für den Ort {city} sind {city_to_postal_codes[city]}')
    else:
        print(f'Unbekanntes Kommando: {option}')
