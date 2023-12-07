def main():


    with open('zuordnung_plz_ort.csv', 'r') as pc_file:
        postal_codes = dict()
        raw_data = pc_file.readlines()
        raw_data_without_header = raw_data[1:]
        for row in raw_data_without_header:
            data = row.split(',')
            postal_code = data[3]
            city = data[2]
            postal_codes[postal_code] = city # Hinzufügen des Wertes city unter dem key postal_code
        

main()