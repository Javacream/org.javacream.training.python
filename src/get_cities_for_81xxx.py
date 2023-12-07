def main():

    def read(source):
        print("step1: read data")
        with open(source, 'r', encoding='utf8') as pc_file:
            raw_data = pc_file.readlines()
        return raw_data
    
    def prepare(raw_data):
        print("step2: prepare data")
        postal_codes = {}
        raw_data_without_header = raw_data[1:]
        for row in raw_data_without_header:
            data = row.split(',')
            postal_code = data[3]
            city = data[2]
            postal_codes[postal_code] = city
        return postal_codes
    
    def analyse(data):
        print("step3: analyse data")
        result_list = []
        for key in data.keys(): #keys() liefert ein set der Postleitzahlen
            if key.startswith('81'):
                city = data.get(key)
                result = key + "=" + city + '\n'
                result_list.append(result)
        #return result_list

        return  [key + "=" + data.get(key) + '\n' for key in data.keys() if key.startswith('81') ]
    def write(result, target):
        print("step4: write result")
        with open(target, 'w', encoding='utf8') as outfile:
            outfile.writelines(result)

    raw_data = read('zuordnung_plz_ort.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'cities_for_81xxx.txt')

main()