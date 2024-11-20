while True:
    name = input('Bitte Namen eingeben: ')
    age = int(input('Bitte Alter eingeben: '))
    if (age < 0):
        print(f'Das eingegebene Alter {age} muss größer 0 sein')
        continue
    if (age > 150):
        print(f'Das eingegebene Alter {age} muss kleiner 150 sein')
        continue
    output_message = f'{name} mit einem Alter von {age} ist'
    if age <= 18:
        print(f'{output_message} jugendlich')
    elif age < 65:
        print(f'{output_message} erwachsen')
    else:
        print(f'{output_message} im Rentenalter')
    again = input('nochmal? j|n: ')
    if again == 'n':
        break