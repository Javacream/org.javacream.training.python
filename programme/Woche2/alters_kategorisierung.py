age = int(input('Bitte Alter eingeben: '))

if age <= 18:
    print(f'{age} ist jugendlich')
elif age < 65:
    print(f'{age} ist erwachsen')
else:
    print(f'{age} ist Rentenalter')
