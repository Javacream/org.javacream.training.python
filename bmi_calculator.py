UNDERWEIGHT_LIMIT = 18
NORMALWEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30
MIN_HEIGHT = 0.7
MAX_HEIGHT = 2.75
MIN_WEIGHT = 40
MAX_WEIGHT = 200
MIN_BMI = 14
MAX_BMI = 45
people_data = [
    {'name': 'Hugo', 'gender': 'm', 'weight': 76.6, 'height': 1.83},
    {'name': 'Emil', 'gender': 'm', 'weight': 76.6, 'height': 1.63},
    {'name': 'Andrea', 'gender': 'd', 'weight': 66.6, 'height': 1.66},
    {'name': 'Donatella', 'gender': 'd', 'weight': 96.6, 'height': 1.66},
    {'name': 'Helga', 'gender': 'w', 'weight': 56.6, 'height': 1.93},
    {'name': 'Hannah', 'gender': 'w', 'weight': 56.6, 'height': 1.81}
]
underweighted = list()
normalweighted = list()
overweighted = list()
obese = list()

for person in people_data:
    name = person['name']
    weight = person['weight']
    height = person['height']
    if height < MIN_HEIGHT or height > MAX_HEIGHT:
        print(f'Unzulässige Körpergröße {height} für {name}, muss zwischen {MIN_HEIGHT} und {MAX_HEIGHT} liegen!')
    elif weight < MIN_WEIGHT or weight > MAX_WEIGHT:
        print(f'Unzulässiges Körpergewicht {weight} für {name}, muss zwischen {MIN_WEIGHT} und {MAX_WEIGHT} liegen!')
    else:
        body_mass_index = weight/(height**2)
        if body_mass_index < MIN_BMI or body_mass_index > MAX_BMI:
            print(f'Berechneter BMI {body_mass_index:.2f} für {name} ist außerhalb des gültigen Bereiches [{MIN_BMI}, {MAX_BMI}]')
        else:
            if body_mass_index < UNDERWEIGHT_LIMIT:
                underweighted.append(name)
            elif body_mass_index >= UNDERWEIGHT_LIMIT and body_mass_index <= NORMALWEIGHT_LIMIT:
                normalweighted.append(name)
            elif body_mass_index > NORMALWEIGHT_LIMIT and body_mass_index < OVERWEIGHT_LIMIT:
                overweighted.append(name)
            else:
                obese.append(name)
print(f'Untergewicht: Anzahl {len(underweighted)}, Personen {underweighted}')
print(f'Normalgewicht: Anzahl {len(normalweighted)}, Personen {normalweighted}')
print(f'Übergewicht: Anzahl {len(overweighted)}, Personen {overweighted}')
print(f'Fettleibig: Anzahl {len(obese)}, Personen {obese}')
