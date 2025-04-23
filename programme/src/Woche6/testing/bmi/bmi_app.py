from bmi import calculate_bmi
def get_height():
    person_height = input('Bitte geben Sie ihre Körpergröße in Zentimetern an: ')
    person_height = int(person_height)
    return person_height
def get_weight():
    person_weight = input('Bitte geben Sie ihr Körpergewicht in Kilogramm an: ')
    person_weight = float(person_weight)
    return person_weight

def main():
    weight = get_weight()
    height = get_height()
    calculated_bmi = calculate_bmi(weight, height)
    print(calculated_bmi)

main()