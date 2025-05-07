UNDERWEIGHT_LIMIT = 18
NORMALWEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30
MIN_HEIGHT = 0.7
MAX_HEIGHT = 2.75
MIN_WEIGHT = 40
MAX_WEIGHT = 200
MIN_BMI = 14
MAX_BMI = 45
with open('people.txt', 'rt', encoding='utf-8') as people_file: 
    lines =  people_file.readlines()
people_data = list()
for line in lines:
    line = line.replace('\n', '')    
    splitted = line.split(';')
    name = splitted[0]
    weight = float(splitted[2])
    height = float(splitted[3])
    person_data = {'name': name, 'weight': weight, 'height': height}
    people_data.append(person_data)

underweighted = list()
normalweighted = list()
overweighted = list()
obese = list()
invalid = list()
for person in people_data:
    name = person['name']
    weight = person['weight']
    height = person['height']
    if height < MIN_HEIGHT or height > MAX_HEIGHT:
        invalid.append(f'Unzulässige Körpergröße {height} für {name}, muss zwischen {MIN_HEIGHT} und {MAX_HEIGHT} liegen!')
    elif weight < MIN_WEIGHT or weight > MAX_WEIGHT:
        invalid.append(f'Unzulässiges Körpergewicht {weight} für {name}, muss zwischen {MIN_WEIGHT} und {MAX_WEIGHT} liegen!')
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
with open('people_bmi_analysis_result.txt', 'wt', encoding='utf-8') as result_file:
    result_file.write(f'Ungültig: Anzahl {len(invalid)}, Personen {invalid}\n')
    result_file.write(f'Untergewicht: Anzahl {len(underweighted)}, Personen {underweighted}\n')
    result_file.write(f'Normalgewicht: Anzahl {len(normalweighted)}, Personen {normalweighted}\n')
    result_file.write(f'Übergewicht: Anzahl {len(overweighted)}, Personen {overweighted}\n')
    result_file.write(f'Fettleibig: Anzahl {len(obese)}, Personen {obese}')
