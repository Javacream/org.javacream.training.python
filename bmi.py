UNDERWEIGHT_LIMIT = 18.5
NORMALWEIGHT_LIMIT = 22
OVERWEIGHT_LIMIT = 30
name = input('please enter your name: ')
weight = input(f'{name}, please enter your weight in kg: ')
height = input(f'{name}, please enter your height in cm: ')
weight = float(weight)
height = int(height)
height = height / 100
body_mass_index = weight/(height*height)
if body_mass_index < UNDERWEIGHT_LIMIT:
    bmi_category = 'underweighted'
elif body_mass_index < NORMALWEIGHT_LIMIT:
    bmi_category = 'normal weighted'
elif body_mass_index < OVERWEIGHT_LIMIT:
    bmi_category = 'overweighted'
else:
    bmi_category = 'obese'


print(f'{name} with a weight of {weight}kg and a height of {height:.2f}m has a bmi of {body_mass_index:.2f} and is {bmi_category}')