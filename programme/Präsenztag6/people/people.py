import os
import file_util

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

def create_people_result(people_data):
    return [f'{person["firstname"]} {person["lastname"]} ist {person["weight"]}kg schwer und {person["height"]} cm groß\n' for person in people_data]

def calculate_backup_number(backup_dir):
    return len(os.listdir(backup_dir)) + 1

def write_people_data(result):
    file_util.write_data(f'result/people_result.txt', result)
def prepare():
    RESULT_DIR = 'result'
    BACKUP_DIR = 'backup'
    RESULT_FILE = 'people_result.txt'

    file_util.prepare_dir(RESULT_DIR)
    file_util.prepare_dir(BACKUP_DIR)
    if file_util.check_file_exists(f'{RESULT_DIR}/{RESULT_FILE}'):
        backup_number = calculate_backup_number(BACKUP_DIR)
        os.rename(f'{RESULT_DIR}/{RESULT_FILE}', f'{BACKUP_DIR}/people_result_{backup_number}.bak')
