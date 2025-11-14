def calculate_bmi(weight, height):
    height = height / 100
    bmi = weight / (height**2)
    return bmi

def main():
    person_weight = 76.5
    person_height = 183
    calculated_bmi = calculate_bmi(person_weight, person_height) # implizit weight = person_weight und height = person_height
    print(f'{calculated_bmi:.2f}')

main()