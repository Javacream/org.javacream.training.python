while True:
    try:
        age = input('Bitte Alter eingeben: ')
        age = int(age)
        if age < 0:
            print(f'negatives Alter {age} ist nicht zulässig')
        elif age > 150:
             print(f'so ein Alter ist nicht erreichbar: {age}')
        else:     
            if age < 18:
                print(f'{age } ist ein jugendliches Alter')
            elif age < 65:
                print(f'{age} ist ein erwachsenes Alter')
            else:
                print(f'{age} ist Rentenalter')    

    except Exception as e:
        print (f'*** Fehler bei der Alterskategorisierung: {e}')
    
    again = input("Zum Beenden des Programms 'n' eingeben: ")
    if again == 'n':
        break