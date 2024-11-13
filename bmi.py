# Dieses Programm berechnet einen BMI für die Person Meier mit Körpergewicht 74.1 und Körpergröße 183cm

name = 'Meier'
weight = 74.1
height = 183 

bmi = weight / (height * height) * 100 * 100 # Berechnung des BMI

print (f'Die Person namens {name} hat mit einem Gewicht von {weight} und einer Körpergröße von {height}cm einen BMI von {bmi}')

print(type(name), type(weight), type(height), type(bmi))