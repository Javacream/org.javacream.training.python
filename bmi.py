def input_height():
        height = input('Please enter your height: ')
        height = int(height)
        return height
def input_weight():
        weight = input('Please enter your weight: ')
        weight = float(weight)
        return weight
def input_name():
     return input('Please enter your name: ')

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
    print(f'the person {name} is {bmi_category}')
     
def main():
    while True:
        height = input_height()
        weight = input_weight()
        name = input_name()
        body_mass_index = calculate_bmi(height, weight)
        bmi_category = categorize_bmi(body_mass_index)
        print_bmi(name, bmi_category)
        again = input('again?.')    
        if again == 'n':
            break

main()