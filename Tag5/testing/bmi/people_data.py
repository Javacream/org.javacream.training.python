import os
import csv

class Person:
    def __init__(self, name, weight, height, gender):
        self.name = name
        self.weight = weight
        self.height = height
        self.gender = gender
def read_person_data(path):
    people = list()
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as file:
            reader = csv.reader(file)
            for person_data in reader:
                person= Person(person_data[0], float(person_data[1]), float(person_data[2]), person_data[3])
                people.append(person)
            return people
    else:
        print(f"Datei {path} nicht gefunden")
    return people
def write_person_data(path, result_list):
    with open(path, 'wt', encoding='utf-8') as file:
        file.writelines([f'{result}\n' for result in result_list])
