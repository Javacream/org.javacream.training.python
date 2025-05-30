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

with open('programme/Präsenztag2/people.txt', encoding='utf-8') as people_file:
    content = people_file.readlines()
# print(len(content))
for row in content:
    row_length = len(row)
    if row[row_length -1] == '\n':
        row = row[0:row_length -1]
    name = row[0:19]
    weight = float(row[20:26])
    height = int(row[27:31])
    if weight <= MIN_WEIGHT or weight > MAX_WEIGHT:
        result = f'Das für {name} eingelesene Körpergewicht {weight} ist außerhalb des gültigen Bereichs {MIN_WEIGHT}-{MAX_WEIGHT}'
    elif height <= MIN_HEIGHT or height > MAX_HEIGHT:
        result = f'Die für {name} eingelesene Körpergröße {height} ist außerhalb des gültigen Bereichs {MIN_HEIGHT}-{MAX_HEIGHT}'
    else:
        body_mass_index = weight / (height/100 * height/100)
        if body_mass_index < MIN_BMI or body_mass_index > MAX_BMI:
            result = f'Der für {name} berechnete Body Mass Index von {body_mass_index:.2f} ist unplausibel, muss zwischen {MIN_BMI} und {MAX_BMI} liegen'        
        else:
            if body_mass_index < UNDERWEIGHT_LIMIT:
                category = 'untergewichtig'
            elif body_mass_index < NORMALWEIGHT_LIMIT:
                category = 'normalgewichtig'
            elif body_mass_index < OVERWEIGHT_LIMIT:
                category = 'übergewichtig'
            else:
                category = 'fettleibig'
            result = f'{name} ist mit einem Body Mass Index von {body_mass_index:.2f} {category}'

    with open ('programme/Präsenztag2/people_bmi.txt', 'at', encoding='utf-8') as file:
        file.write(f'{result}\n')