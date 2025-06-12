def read_postal_codes(path):
    with open(path, 'rt', encoding='utf-8') as file:
        lines = file.readlines()
    return [l.replace('\n', '') for l in lines]
   
def create_postal_codes_to_city(lines):
    postal_codes_to_city = dict()
    for line in lines:
        splitted = line.split('=')
        postal_codes_to_city[splitted[0]] = splitted[1]
    return postal_codes_to_city
def create_city_to_postal_codes(lines):
    city_to_postal_codes = dict()
    for line in lines:
        splitted = line.split('=')
        postal_code = splitted[0]
        city = splitted[1]
        if city in city_to_postal_codes:
            city_to_postal_codes[city].append(postal_code)
        else:
            postal_codes = []
            postal_codes.append(postal_code)
            city_to_postal_codes[city] = postal_codes
    return city_to_postal_codes
def print_city_for_postal_code(postal_code_to_city, postal_code):
    print(f'city for postal code {postal_code} is {postal_code_to_city[postal_code]}')
def print_postal_codes_for(city_to_postal_codes, city):
    print(f'postalcodes for city {city} is {city_to_postal_codes[city]}')

def print_number_of_cities(city_to_postal_codes):
    print(f'{len(city_to_postal_codes)} distinct cities {set(city_to_postal_codes.keys())} known')
def main():
    file_name =  './programme/Präsenztag4/postal_codes.txt'
    lines = read_postal_codes(file_name)
    postal_code_to_city = create_postal_codes_to_city(lines)
    city_to_postal_codes = create_city_to_postal_codes(lines)
    postal_code = "81371"
    print_city_for_postal_code(postal_code_to_city, postal_code)
    print_number_of_cities(city_to_postal_codes)
    print_postal_codes_for(city_to_postal_codes, 'München')
    print_postal_codes_for(city_to_postal_codes, 'Berlin')


main()