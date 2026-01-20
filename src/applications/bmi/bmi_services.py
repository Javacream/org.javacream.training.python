def read_people_data(path):
    with open(path, 'rt', encoding='utf-8') as file:
        content = file.read()
    return content.split('\n')

def calculate_bmi(height, weight):
    height = height/100
    return weight/(height**2)

def calculate_bmi_category(bmi):
    if bmi < 18.5:
        bmi_category = 'underweight'
    elif bmi < 25:
        bmi_category = 'normalweight'
    elif bmi < 30:
        bmi_category = 'overweight'
    else:
        bmi_category = 'obese'
    return bmi_category
def calculate_result_text(name, height, weight, bmi, bmi_category):
    return f'{name} with weight {weight} and height {height} has a bmi of {bmi:.2f} and is therefor {bmi_category}'

def extract(raw_data):
    data = raw_data.split(',')
    return (data[0], int(data[1]), float(data[2]))
def write(path, result):
    with open(path, 'at', encoding='utf-8') as file:
        file.write(f'{result}\n')
