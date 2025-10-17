MIN_ADULT_AGE = 18
MAX_ADULT_AGE = 65
MIN_AGE = 0
MAX_AGE = 130
while True:
    name = input('Bitte Namen eingeben: ')
    age = input(f'Bitte Alter für {name} eingeben: ')
    try:
        age = int(age)
        if (age >= MIN_AGE) and (age <= MAX_AGE):
            prefix = f'{name} ist mit einem Alter von {age} Jahren'
            if age < MIN_ADULT_AGE:
                print(f'{prefix} jugendlich')
            elif age < MAX_ADULT_AGE:
                print(f'{prefix} erwachsen')
            else:
                print(f'{prefix} im Rentenalter')
        else:
            print(f'das eingegebene Alter ({age}) ist nicht im gültigen Bereich [{MIN_AGE}, {MAX_AGE}]')
    except Exception as e:
        print(f'Alterskategorisierung für {name} nicht möglich, "{age}" kann nicht als Zahl interpretiert werden!')
    again = input('Nochmal? j|n? ')
    if (again != 'j'):
        break