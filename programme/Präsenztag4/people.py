def read_lines(path):
    with open(path, 'rt', encoding='utf-8') as people_csv_file:
        rows_with_cr = people_csv_file.readlines()
    rows = []
    for row_with_cr in rows_with_cr:
        rows.append(row_with_cr.replace('\n', ''))
    return rows

def print_people_data(people_data):
    for actual_row in people_data:
        list_of_person_data = actual_row.split(',')  
        # print(f'{list_of_person_data[0]} {list_of_person_data[1]} ist {float(list_of_person_data[2])}kg schwer und {int(list_of_person_data[3])} cm groß')
        firstname = list_of_person_data[0]
        lastname = list_of_person_data[1]
        weight = float(list_of_person_data[2])
        height = int(list_of_person_data[3])
        print(f'{firstname} {lastname} ist {weight}kg schwer und {height} cm groß')

def main():
    file_name =  './programme/Präsenztag4/people.csv'
    lines = read_lines(file_name)# Implizit wird hier beim Aufruf die Anweisung path = file_name ausgeführt
    print_people_data(lines)
    print('done')

main()  