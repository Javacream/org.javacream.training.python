def read_dictionary(path):
    cities_postal_codes_dict = dict()
    with open (path, encoding='utf-8') as file:
     rows = file.readlines()
     rows = [row[:-1] for row in rows if not row == '\n']
     for row in rows:
        splitted = row.split("=")
        postalcode = splitted[0]
        city = splitted[1]
        postalcodes_list = cities_postal_codes_dict.get(city)
        if postalcodes_list == None:
           postalcodes_list = []
           cities_postal_codes_dict[city] = postalcodes_list
        postalcodes_list.append(postalcode)
     return cities_postal_codes_dict      
def postalcodes_for(data, city):
   return data.get(city, [])
   return 
def main():
    data = read_dictionary('postalcodes_and_cities.txt')
    city = input ('Bitte geben Sie eine Stadt ein: ')
    print(postalcodes_for(data, city))
main()