age = input('Bitte Alter eingeben: ')
age = int(age)

if age < 18:
    print('jugendlich')
elif age < 65:
    print('erwachsen')
else:
    print('Rentenalter')    
