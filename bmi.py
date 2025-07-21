height = input('Please enter your height: ')
weight = input('Please enter your weight: ')
name = input('Please enter your name: ')
height = int(height)
weight = float(weight)
body_mass_index = weight /(height*height) * 10000

if body_mass_index < 18:
    bmi_category = 'underweight'
if body_mass_index >= 18 and body_mass_index < 25:
    bmi_category = 'normalweight'
if body_mass_index >= 25 and body_mass_index < 30:
    bmi_category = 'overweight'
if body_mass_index >= 30:
    bmi_category = 'obese'

print(f'the person {name} is {bmi_category}')