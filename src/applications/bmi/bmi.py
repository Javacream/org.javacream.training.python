def get_name():
    return input('enter your name: ')

def get_height():
    height = input('enter your height in cm: ')
    height = int(height)
    return height

def get_weight():
    weight = input('enter your weight in kg: ')
    weight = float(weight)
    return weight

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


def main():
    name = get_name()
    height = get_height()
    weight = get_weight()
    bmi = calculate_bmi(height, weight)
    bmi_category = calculate_bmi_category(bmi)
    result = calculate_result_text(name, height, weight, bmi, bmi_category)
    print(result)

main()