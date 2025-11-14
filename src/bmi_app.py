def get_data():
    with open('data/people_data.txt', encoding='utf-8') as file:
        return file.read().split('\n')

def get_people_data(data: list):
    people = []
    for person_data in data:
        firstname, lastname, weight, height = person_data.split(',')
        weight = float(weight)
        height = int(height)
        people.append((firstname, lastname, weight, height))
    return people    

def get_people_result(people: list):
    descriptions = []
    for person in people:
        firstname, lastname, weight, height = person
        description = get_description(firstname, lastname, weight, height)
        descriptions.append(description)
    return descriptions

def get_description(firstname: str, lastname: str, weight: float, height: int):
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    return f'{firstname} {lastname} with weight {weight}kg and height {height}cm has a body mass index of {bmi:.2f} and is therefor {category}'

def calculate_bmi(weight: float, height: int):
    height = height / 100
    bmi = weight / (height**2)
    return bmi

def categorize_bmi(body_mass_index: float):
    UNDERWEIGHT_LIMIT = 18.5
    NORMALWEIGHT_LIMIT = 25
    OVERWEIGHT_LIMIT = 30

    if body_mass_index < UNDERWEIGHT_LIMIT:
        bmi_category = 'underweighted'
    elif body_mass_index < NORMALWEIGHT_LIMIT:
        bmi_category = 'normal weighted'
    elif body_mass_index < OVERWEIGHT_LIMIT:
        bmi_category = 'overweighted'
    else:
        bmi_category = 'obese'
    return bmi_category

def write_result(descriptions: list):
    out_descriptions = [f'{description}\n' for description in descriptions]
    result_outpath = 'data/people_bmi_descriptions.txt'
    with open(result_outpath, 'wt', encoding='utf-8') as file:
        file.writelines(out_descriptions)
def main():
    raw_data = get_data()
    people_data = get_people_data(raw_data)
    people_result = get_people_result(people_data)
    write_result(people_result)
main()