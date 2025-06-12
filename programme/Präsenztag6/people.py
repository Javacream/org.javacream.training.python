import os

RESULT_DIR = 'result'
BACKUP_DIR = 'backup'
RESULT_FILE = 'people_result.txt'

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

def write_people_data(people_data):
    with open(f'{RESULT_DIR}/{RESULT_FILE}', 'wt', encoding='utf-8') as file:
        file.writelines([f'{person["firstname"]} {person["lastname"]} ist {person["weight"]}kg schwer und {person["height"]} cm groß\n' for person in people_data])

def check_file_exists(path):
    return os.path.exists(path)


def prepare_result_dir():
    if not os.path.isdir(RESULT_DIR):
        os.mkdir(RESULT_DIR)

def prepare_backup_dir():
    if not os.path.isdir(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

def check_existing_resultfile():
    return os.path.exists(f'{RESULT_DIR}/{RESULT_FILE}')

def calculate_backup_number():
    return len(os.listdir(BACKUP_DIR)) + 1

def prepare():
    prepare_result_dir()
    prepare_backup_dir()
    if check_existing_resultfile():
        backup_number = calculate_backup_number()
        os.rename(f'{RESULT_DIR}/{RESULT_FILE}', f'{BACKUP_DIR}/people_result_{backup_number}.bak')

def main():
    file_name =  './data/people.csv'
    if check_file_exists(file_name):
        prepare()
        lines = read_lines(file_name)
        people = create_people_data(lines)
        write_people_data(people)
    else:
        print(f'input file {file_name} does not exist in {os.getcwd().replace('\\', '/')}')
    print('done')

main()  