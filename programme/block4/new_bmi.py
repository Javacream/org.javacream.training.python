import json
def read_data(inpath):
    with open(inpath, encoding='utf-8') as file:
        return json.load(file) 

def calculate_bmis(people_data):
    bmis = []
    for person_data in people_data:
        bmi = calculate_bmi(person_data['height']/100, person_data['weight'])
        bmis.append((person_data['name'], bmi))
    return bmis

def calculate_bmi(height, weight):
    return weight/height**2

def write_result(outpath, bmi_infos):
    with open(outpath, 'wt', encoding='utf-8') as file:
        for bmi_info in bmi_infos:
            file.write(f'{bmi_info}\n')
def main():
    inpath = 'data/people_data.json'
    people_data = read_data(inpath)
    bmi_infos = calculate_bmis(people_data)
    outpath = 'data/bmi_categories.txt'
    write_result(outpath, bmi_infos)

main()