
name = input('please enter your name: ')
height = input('please enter your height in cm (numbers only!): ')
weight = input('please enter your weight in kg(numbers and one . only): ')
height = int(height)
weight = float(weight)
body_mass_index = weight/(height*height)* 100 * 100
print(f'{name} with a height of {height}cm and weight of {weight}kg has a BMI of {body_mass_index:.2f}')