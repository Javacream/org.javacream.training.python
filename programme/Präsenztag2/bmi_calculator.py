# Dieses Programm berechnet einen Body-Mass-Index
name = input('Bitte geben Sie Ihren Namen an: ')
weight = input('Bitte geben Sie Ihr Körpergewicht in Kilogramm an, Kommazeichen ist der Punkt: ')
height = input('Bitte geben Sie Ihre Körpergröße in cm an: ')
weight = float(weight)
height = int(height)
body_mass_index = weight / (height/100 * height/100)
if body_mass_index < 18:
    category = 'untergewichtig'
elif body_mass_index < 25:
    category = 'normalgewichtig'
elif body_mass_index < 30:
    category = 'übergewichtig'
else:
    category = 'fettleibig'
print(f'{name} ist mit einem Body Mass Index von {body_mass_index:.2f} {category}')