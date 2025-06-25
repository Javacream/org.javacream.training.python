name = input('Enter your name: ')
weight  = input('Enter your weight in kg: ') 
height  = input('Enter your height in cm: ') 

weight = float(weight)
height = int(height)
height = height / 100 
bmi = weight / (height * height) 

print(f'{name} has a body mass index of {bmi:.2f}')