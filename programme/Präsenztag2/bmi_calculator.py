# Dieses Programm berechnet einen Body-Mass-Index
name = input('Bitte geben Sie Ihren Namen an: ')
weight = input('Bitte geben Sie Ihr Körpergewicht in Kilogramm an, Kommazeichen ist der Punkt: ')
height = input('Bitte geben Sie Ihre Körpergröße in cm an: ')
weight = float(weight)
height = int(height)
if weight <= 5 or weight > 450:
    print(f'Das eingegebene Körpergewicht {weight} ist außerhalb des gültigen Bereichs 5-450' )
elif height <= 50 or height > 250:
    print(f'Die eingegebene Körpergröße {height} ist außerhalb des gültigen Bereichs 50-250' )
else:
    body_mass_index = weight / (height/100 * height/100)
    if body_mass_index < 12 or body_mass_index > 45:
        print(f'Der für {name} berechnete Body Mass Index von {body_mass_index:.2f} ist unplausibel, muss zwischen 12 und 45 liegen')        
    else:
        if body_mass_index < 18:
            category = 'untergewichtig'
        elif body_mass_index < 25:
            category = 'normalgewichtig'
        elif body_mass_index < 30:
            category = 'übergewichtig'
        else:
            category = 'fettleibig'
        print(f'{name} ist mit einem Body Mass Index von {body_mass_index:.2f} {category}')