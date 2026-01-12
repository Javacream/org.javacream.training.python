name = input('Please enter your name: ')
weight = input(f'{name}, please enter your weight in kg: ')
height = input(f'{name}, please enter your height in cm: ')
weight = float(weight) 
height = int(height)
height = height / 100
bmi = weight / (height**2)
print(f'{name} with weight {weight} and height {height} has a bmi of {bmi:.2f}')