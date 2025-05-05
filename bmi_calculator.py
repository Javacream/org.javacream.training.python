UNDERWEIGHT_LIMIT = 18
NORMALWEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30
MIN_HEIGHT = 0.7
MAX_HEIGHT = 2.75
MIN_WEIGHT = 40
MAX_WEIGHT = 200
MIN_BMI = 14
MAX_BMI = 45
name = input("Bitte Name eingeben: ")
weight = input("Bitte Körpergewicht in kg: ")
height = input("Bitte Körpergröße in Meter: ")
weight = float(weight)
height = float(height)
if height < MIN_HEIGHT or height > MAX_HEIGHT:
    print(f'Unzulässige Körpergröße {height}, muss zwischen {MIN_HEIGHT} und {MAX_HEIGHT} liegen!')
elif weight < MIN_WEIGHT or weight > MAX_WEIGHT:
    print(f'Unzulässiges Körpergewicht {weight}, muss zwischen {MIN_WEIGHT} und {MAX_WEIGHT} liegen!')
else:
    body_mass_index = weight/(height**2)
    if body_mass_index < MIN_BMI or body_mass_index > MAX_BMI:
        print(f'Berechneter BMI {body_mass_index} ist außerhalb des gültigen Bereiches [{MIN_BMI}, {MAX_BMI}]')
    else:
        if body_mass_index < UNDERWEIGHT_LIMIT:
            print(f'{name} ist untergewichtig')
        elif body_mass_index >= UNDERWEIGHT_LIMIT and body_mass_index <= NORMALWEIGHT_LIMIT:
            print(f'{name} ist normalgewichtig')
        elif body_mass_index > NORMALWEIGHT_LIMIT and body_mass_index < OVERWEIGHT_LIMIT:
            print(f'{name} ist übergewichtig')
        else:
            print(f'{name} ist fettleibig')
