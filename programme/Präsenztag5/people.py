def read_lines(path):
    with open(path, 'rt', encoding='utf-8') as people_csv_file:
        rows_with_cr = people_csv_file.readlines()
    rows = []
    for row_with_cr in rows_with_cr:
        rows.append(row_with_cr.replace('\n', ''))
    return rows

def create_people_data(lines):
    people = []
    for actual_line in lines:
        list_of_person_data = actual_line.split(',')  
        firstname = list_of_person_data[0]
        lastname = list_of_person_data[1]
        weight = float(list_of_person_data[2])
        height = int(list_of_person_data[3])
        person = {'firstname': firstname, 'lastname': lastname, 'height': height, 'weight': weight}
        people.append(person)
    return people

def print_people_data(people_data):
    for person in people_data:
        print(f'{person["firstname"]} {person["lastname"]} ist {person["weight"]}kg schwer und {person["height"]} cm groß')

def main():
    file_name =  './programme/Präsenztag4/people.csv'
    lines = read_lines(file_name)# Implizit wird hier beim Aufruf die Anweisung path = file_name ausgeführt
    people = create_people_data(lines)
    print_people_data(people)
    print('done')

main()  