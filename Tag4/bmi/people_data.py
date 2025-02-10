def read_person_data(path):
    with open(path, encoding='utf-8') as file:
        rows = file.readlines()
        cleaned_rows = [row[:-1] for row in rows if not row == '\n']
        people = list()
        for row in cleaned_rows:
            person_data = row.split(',')
            person_dict = {'name': person_data[0], 'weight': float(person_data[1]), 'height': float(person_data[2])}
            people.append(person_dict)
        return people
def write_person_data(path, result_list):
    with open(path, 'wt', encoding='utf-8') as file:
        file.writelines([f'{result}\n' for result in result_list])
