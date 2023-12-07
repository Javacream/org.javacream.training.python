def main():
    postal_codes = dict()

    def input_postal_code_or_exit():
        invalid = True
        while invalid:
            user_input = input('Enter 5 digit postal code er "exit": ')
            if user_input.lower() == 'exit':
                break
            elif len(user_input) == 5 and user_input.isnumeric():
                invalid = False
                return user_input
            else:
                print(f'postal code must be 5 digits, you entered {user_input}')
    def extract_postal_code_and_city(raw_data):
        data_without_header = raw_data[1:]
        postal_code_and_city = list()
        for row in data_without_header:
            data = row.split(',')
            postal_code = data[3]
            city = data[2]
            postal_code_and_city.append((postal_code, city))
        return postal_code_and_city

    def fill_dictionary(data):
        for postal_code_and_city in data:
            postal_codes[postal_code_and_city[0]] =postal_code_and_city[1]
    def output_result(postal_code, city):
        if city != None:
            print(f'postal code {postal_code} is city {city}')
        else:
            print(f'postal code {postal_code} is invalid')
    def read_file():
        with open('zuordnung_plz_ort.csv', 'r') as plz_file:
            return plz_file.readlines()

    raw_data = read_file()
    data = extract_postal_code_and_city(raw_data)
    fill_dictionary(data)

    while True:
        postal_code = input_postal_code_or_exit()
        if postal_code == None:
            break
        city = postal_codes.get(postal_code)
        output_result(postal_code, city)

main()