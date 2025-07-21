while True:
    height = input('Please enter your height: ')
    weight = input('Please enter your weight: ')
    name = input('Please enter your name: ')
    height = int(height)
    weight = float(weight)
    body_mass_index = weight /(height*height) * 10000
    if body_mass_index < 18:
        bmi_category = 'underweight'
    elif body_mass_index < 25:
        bmi_category = 'normalweight'
    elif body_mass_index < 30:
        bmi_category = 'overweight'
    else:
        bmi_category = 'obese'

    print(f'the person {name} is {bmi_category}')

    again = input('again?.')
    if again == 'n':
        break