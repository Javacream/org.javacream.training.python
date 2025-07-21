height = input('Please enter your height: ')
weight = input('Please enter your weight: ')
name = input('Please enter your name: ')
height = int(height)
weight = float(weight)
body_mass_index = weight /(height*height) * 10000
print(f'the person {name} has a body mass index of {body_mass_index:.2f}')