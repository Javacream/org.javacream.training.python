name = input('please enter your name: ')
weight = input(f'{name}, please enter your weight in kg: ')
height = input(f'{name}, please enter your height in cm: ')
weight = float(weight)
height = int(height)
height = height / 100
body_mass_index = weight/(height*height)
print(f'the calculated bmi for {name} is: {body_mass_index:.2f}')