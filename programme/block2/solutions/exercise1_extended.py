MIN_ADULT_AGE = 18
MAX_ADULT_AGE = 65
MIN_AGE = 0
MAX_AGE = 150

while True:
    try:
        name = input('Bitte geben Sie Ihren Namen an: ')
        age = input('Bitte Alter eingeben: ')
        age = int(age)
        if age < MIN_AGE:
            print(f'negatives Alter {age} ist nicht zulässig')
        elif age > MAX_AGE:
             print(f'so ein Alter ist nicht erreichbar: {age}')
        else:     
            if age < MIN_ADULT_AGE:
                age_category = "jugendlich"
            elif age < MAX_ADULT_AGE:
                age_category = "erwachsen"
            else:
                age_category = 'im Rentenalter'    

            print(f'{name} ist {age_category}')
    except Exception as e:
        print (f'*** Fehler bei der Alterskategorisierung: {e}')
    
    again = input("Zum Beenden des Programms 'n' eingeben: ")
    if again == 'n':
        break