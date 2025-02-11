import os
import csv
import bmi as bmi_module
class Person:
    def __init__(self, name, weight, height, gender):
        self.name = name
        self.weight = weight
        self.height = height
        self.gender = gender

data_counter = 0
people_in_categories = dict()
people_in_categories['untergewichtig'] = []
people_in_categories['normalgewichtig'] = []
people_in_categories['übergewichtig'] = []
people_in_categories['fettleibig'] = []
people_by_gender = {'m':[], 'w': [], 'd':[]}

def categorize(person):
    global data_counter
    bmi = bmi_module.calculate_bmi(person.height, person.weight)
    bmi_category = bmi_module.bmi_category_for(bmi)
    people_in_categories[bmi_category].append(person)
    people_by_gender[person.gender].append(f'{person.name} ist {bmi_category}')
    data_counter += 1


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
