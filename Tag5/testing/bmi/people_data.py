import os
import csv
def read_person_data(path):
    people = list()
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as file:
            reader = csv.reader(file)
            for person_data in reader:
                person_dict = {'name': person_data[0], 'weight': float(person_data[1]), 'height': float(person_data[2]), 'gender':person_data[3]}
                people.append(person_dict)
            return people
    else:
        print(f"Datei {path} nicht gefunden")
    return people
def write_person_data(path, result_list):
    with open(path, 'wt', encoding='utf-8') as file:
        file.writelines([f'{result}\n' for result in result_list])
