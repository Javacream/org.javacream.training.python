def read_dictionary(path):
    postalcodes_cities_dict = dict()
    with open (path, encoding='utf-8') as file:
     rows = file.readlines()
     rows = [row[:-1] for row in rows if not row == '\n']
     for row in rows:
        splitted = row.split("=")
        postalcodes_cities_dict[splitted[0]] = splitted[1]
     return postalcodes_cities_dict      
def city_for(data, postalcode):
   return data.get(postalcode, 'Unknown')
   return 
def main():
    data = read_dictionary('postalcodes_and_cities.txt')
    postalcode = input ('Bitte geben Sie eine fünfstellige PLZ an: ')
    print(city_for(data, postalcode))
main()