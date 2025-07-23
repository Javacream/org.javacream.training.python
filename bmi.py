def read_people_data():
    # TODO: read people.csv
    return []
def calculate_bmi(height, weight):
     return weight /(height*height) * 10000

def categorize_bmi(bmi):
    if bmi < 18:
        bmi_category = 'underweight'
    elif bmi < 25:
        bmi_category = 'normalweight'
    elif bmi < 30:
        bmi_category = 'overweight'
    else:
        bmi_category = 'obese'
    return bmi_category

def print_bmi(name, bmi_category):
    # TODO: replace with write to file people_bmi.txt print(f'the person {name} is {bmi_category}')
    pass

def main():
    people_data = read_people_data()
    # TODO iteration over people_data, calculate and categorize each person
    body_mass_index = calculate_bmi(height, weight)
    bmi_category = categorize_bmi(body_mass_index)
    print_bmi(name, bmi_category)

main()