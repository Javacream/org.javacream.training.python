def main():


    postal_codes = dict()
    with open('zuordnung_plz_ort.csv', 'r') as pc_file:
        raw_data = pc_file.readlines()
        raw_data_without_header = raw_data[1:]
        for row in raw_data_without_header:
            data = row.split(',')
            postal_code = data[3]
            city = data[2]
            postal_codes[postal_code] = city # Hinzufügen des Wertes city unter dem key postal_code
    while True:    
        user_input = input('enter a 5 digit number: ')
        #if len(user_input) == 5 and user_input.isnumeric()
        city = postal_codes.get(user_input)
        if city != None:
            print(f'city for postal code {user_input} is {city}')
        else:
            print(f'city for postal code {user_input} not found')
              
main()