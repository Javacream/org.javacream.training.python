UNDERWEIGHT_LIMIT = 18
NORMALWEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30
MIN_HEIGHT = 0.7
MAX_HEIGHT = 2.75
MIN_WEIGHT = 40
MAX_WEIGHT = 200
MIN_BMI = 14
MAX_BMI = 45
CATEGORIES = ('invalid', 'underweight', 'normalweight', 'overweight', 'obese')
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

result_dict = dict()
for category in CATEGORIES:
    result_dict[category] = list()

for person in people_data:
    name = person['name']
    weight = person['weight']
    height = person['height']
    if height < MIN_HEIGHT or height > MAX_HEIGHT:
        result_dict['invalid'].append(f'Unzulässige Körpergröße {height} für {name}, muss zwischen {MIN_HEIGHT} und {MAX_HEIGHT} liegen!')
    elif weight < MIN_WEIGHT or weight > MAX_WEIGHT:
        result_dict['invalid'].append(f'Unzulässiges Körpergewicht {weight} für {name}, muss zwischen {MIN_WEIGHT} und {MAX_WEIGHT} liegen!')
    else:
        body_mass_index = weight/(height**2)
        if body_mass_index < MIN_BMI or body_mass_index > MAX_BMI:
            result_dict['invalid'].append(f'Berechneter BMI {body_mass_index:.2f} für {name} ist außerhalb des gültigen Bereiches [{MIN_BMI}, {MAX_BMI}]')
        else:
            if body_mass_index < UNDERWEIGHT_LIMIT:
                category = 'underweight'
            elif body_mass_index >= UNDERWEIGHT_LIMIT and body_mass_index <= NORMALWEIGHT_LIMIT:
                category = 'normalweight'
            elif body_mass_index > NORMALWEIGHT_LIMIT and body_mass_index < OVERWEIGHT_LIMIT:
                category = 'overweight'
            else:
                category = 'obese'
            result_dict[category].append(name)                
with open('people_bmi_analysis_result.txt', 'wt', encoding='utf-8') as result_file:
    for category in CATEGORIES:
        result_file.write(f'{category}: Anzahl {len(result_dict[category])}, Personen {result_dict[category]}\n')        
    