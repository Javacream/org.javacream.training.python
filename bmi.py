name = input('please enter your name: ')
weight = input(f'{name}, please enter your weight in kg: ')
height = input(f'{name}, please enter your height in cm: ')
weight = float(weight)
height = int(height)
height = height / 100
body_mass_index = weight/(height*height)
if body_mass_index < 18.5:
    bmi_category = 'underweighted'
elif body_mass_index < 22:
    bmi_category = 'normal weighted'
elif body_mass_index < 30:
    bmi_category = 'overweighted'
else:
    bmi_category = 'obese'


print(f'{name} with a weight of {weight}kg and a height of {height:.2f}m has a bmi of {body_mass_index:.2f} and is {bmi_category}')