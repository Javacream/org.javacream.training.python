MIN_ADULT_AGE = 18
MAX_ADULT_AGE = 65
while True:
    name = input('Bitte Namen eingeben: ')
    age = input(f'Bitte Alter für {name} eingeben: ')
    age = int(age)
    prefix = f'{name} ist mit einem Alter von {age} Jahren'
    if age < MIN_ADULT_AGE:
        print(f'{prefix} jugendlich')
    elif age < MAX_ADULT_AGE:
        print(f'{prefix} erwachsen')
    else:
        print(f'{prefix} im Rentenalter')
    again = input('Nochmal? j|n? ')
    if (again != 'j'):
        break