# Dieses Programm berechnet einen BMI

name = input('Enter your name: ')
weight = input('Enter your weight: ')
height = input('Enter your height in cm: ')

weight = float(weight)
height = int(height)

bmi = weight / (height * height) * 100 * 100 # Berechnung des BMI

print (f'Die Person namens {name} hat mit einem Gewicht von {weight} und einer Körpergröße von {height}cm einen BMI von {bmi}')
