text = "81371=München,30000=Berlin,40000=Hamburg,81777=München"
postal_code_cities = text.split(',')
city_for_postalcode = dict()
postalcodes_for_city = dict()
for postal_code_city in postal_code_cities:
    postal_code_and_city = postal_code_city.split("=")
    postal_code = postal_code_and_city[0]
    city = postal_code_and_city[1]
    city_for_postalcode[postal_code] = city
    postal_codes = postalcodes_for_city.get(city)
    if postal_codes == None:
        postal_codes = []
        postalcodes_for_city[city] = postal_codes
    postal_codes.append(postal_code)

search_postal_code = input("Bitte PLZ eingeben: ")
search_city = input("Bitte Stadt eingeben: ")

print(f"Die Postleitzahl {search_postal_code} ist {city_for_postalcode.get(search_postal_code, 'unbekannt')}")
print(f'Zur Stadt {search_city} gehören die Postleitzahlen: {postalcodes_for_city.get(search_city, "Keine")}')
