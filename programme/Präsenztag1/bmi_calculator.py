# Dieses Programm berechnet einen Body-Mass-Index
name = input('Bitte geben Sie Ihren Namen an: ')
weight = input('Bitte geben Sie Ihr Körpergewicht in Kilogramm an, Kommazeichen ist der Punkt: ')
height = input('Bitte geben Sie Ihre Körpergröße in cm an: ')
weight = float(weight)
height = int(height)
body_mass_index = weight / (height/100 * height/100)
print(f'{name} hat einen Body Mass Index von {body_mass_index:.2f}')