UNDERWEIGHT_LIMIT = 18.5
NORMALWEIGHT_LIMIT = 22
OVERWEIGHT_LIMIT = 30
MIN_WEIGHT = 2
MAX_WEIGHT = 450
MIN_HEIGHT = 35
MAX_HEIGHT = 275
MIN_BMI = 14
MAX_BMI = 45
while True:
    name = input('please enter your name: ')
    weight = input(f'{name}, please enter your weight in kg between {MIN_WEIGHT} and {MAX_WEIGHT}: ')
    height = input(f'{name}, please enter your height in cm between {MIN_HEIGHT} and {MAX_HEIGHT}: ')
    weight = float(weight)
    height = int(height)
    if height < MIN_HEIGHT or height > MAX_HEIGHT:
        print(f'you entered an invalid height: {height}, should be between {MIN_HEIGHT} and {MAX_HEIGHT}')
    elif weight < MIN_WEIGHT or weight > MAX_WEIGHT:
        print(f'you entered an invalid weight: {weight}, should be between {MIN_WEIGHT} and {MAX_WEIGHT}')
    else:
        height = height / 100
        body_mass_index = weight/(height*height)
        if body_mass_index < MIN_BMI or body_mass_index > MAX_BMI:
            print(f'the calculated bmi {body_mass_index:.2f} for {name} is invalid, should be between {MIN_BMI} and {MAX_BMI}')
        else:
            if body_mass_index < UNDERWEIGHT_LIMIT:
                bmi_category = 'underweighted'
            elif body_mass_index < NORMALWEIGHT_LIMIT:
                bmi_category = 'normal weighted'
            elif body_mass_index < OVERWEIGHT_LIMIT:
                bmi_category = 'overweighted'
            else:
                bmi_category = 'obese'
            print(f'{name} with a weight of {weight}kg and a height of {height:.2f}m has a bmi of {body_mass_index:.2f} and is {bmi_category}')
    again = input('again? (Y|n): ')
    if again == 'n':
        break