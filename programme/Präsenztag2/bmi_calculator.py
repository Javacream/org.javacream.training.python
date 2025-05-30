# Dieses Programm berechnet einen Body-Mass-Index
MIN_WEIGHT = 5
MAX_WEIGHT = 450

MIN_HEIGHT = 50
MAX_HEIGHT = 250

UNDERWEIGHT_LIMIT = 18
NORMALWEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30
MIN_BMI = 12
MAX_BMI = 45
while True:
    name = input('Bitte geben Sie Ihren Namen an: ')
    while True:
        weight = input('Bitte geben Sie Ihr Körpergewicht in Kilogramm an, Kommazeichen ist der Punkt: ')
        try:
            weight = float(weight)
            break
        except:
            print(f'{weight} nicht als Zahl interpretierbar, bitte neu eingeben!')
    while True:
        height = input('Bitte geben Sie Ihre Körpergröße in cm an: ')
        try:
            height = float(height)
            break
        except:
            print(f'{height} nicht als Zahl interpretierbar, bitte neu eingeben!')
    if weight <= MIN_WEIGHT or weight > MAX_WEIGHT:
        print(f'Das eingegebene Körpergewicht {weight} ist außerhalb des gültigen Bereichs {MIN_WEIGHT}-{MAX_WEIGHT}' )
    elif height <= MIN_HEIGHT or height > MAX_HEIGHT:
        print(f'Die eingegebene Körpergröße {height} ist außerhalb des gültigen Bereichs {MIN_HEIGHT}-{MAX_HEIGHT}' )
    else:
        body_mass_index = weight / (height/100 * height/100)
        if body_mass_index < MIN_BMI or body_mass_index > MAX_BMI:
            print(f'Der für {name} berechnete Body Mass Index von {body_mass_index:.2f} ist unplausibel, muss zwischen {MIN_BMI} und {MAX_BMI} liegen')        
        else:
            if body_mass_index < UNDERWEIGHT_LIMIT:
                category = 'untergewichtig'
            elif body_mass_index < NORMALWEIGHT_LIMIT:
                category = 'normalgewichtig'
            elif body_mass_index < OVERWEIGHT_LIMIT:
                category = 'übergewichtig'
            else:
                category = 'fettleibig'
            print(f'{name} ist mit einem Body Mass Index von {body_mass_index:.2f} {category}')
    again = input('Weitere Berechnung (j|n)')
    if again == 'n':
        break            