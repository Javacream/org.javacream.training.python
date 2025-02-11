UNDERWEIGHT_BMI = 18
MAX_NORMAL_BMI = 25
MAX_FAT_BMI = 30

def calculate_bmi(height, weight):
    bmi = weight / (height * height) # height in Metern, nicht wie bisher in cm
    return bmi

def bmi_category_for(bmi):
    if bmi < UNDERWEIGHT_BMI:
        return 'untergewichtig'
    elif bmi < MAX_NORMAL_BMI:
        return 'normalgewichtig'
    elif bmi < MAX_FAT_BMI:
        return 'übergewichtig'
    else:
        return 'fettleibig'
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


def main():
    infile = 'Tag4/bmi/people.txt'
    outfile = 'Tag4/bmi/people_result.txt'

    people_list = read_person_data(infile)
    people_result = list()
    for person in people_list:
        bmi = calculate_bmi(person.height, person.weight)
        bmi_category = bmi_category_for(bmi)
        people_result.append(f'{person.name} ist {bmi_category}')
    write_person_data(outfile, people_result)    
if __name__ == '__main__':
    main()


