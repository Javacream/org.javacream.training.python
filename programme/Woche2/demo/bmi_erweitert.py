UNDERWEIGHT_BMI_LIMIT = 18
OVERWEIGHT_BMI_LIMIT = 25
while True:
    name=input('Bitte geben Sie ihren Namen ein: ')
    height=input('Bitte geben Sie ihre Körpergröße in Zentimetern ein: ')
    weight=input('Bitte geben Sie ihr Gewicht mit einer Nachkommastelle ein (Hinweis: Trennzeichen muss der Punkt sein!): ')
    try:
        height = int(height)
        weight = float(weight)
        bmi=weight/(height*height)*10000
        if bmi < UNDERWEIGHT_BMI_LIMIT:
            weight_category = "untergewichtig"
        elif bmi < OVERWEIGHT_BMI_LIMIT:
            weight_category = "normalgewichtig"
        else:
            weight_category = "übergewichtig"        
        message = f'Die Person namens {name} ist {weight_category}'
        print(message)
    except Exception as e:
        print(f'Fehleingabe, Grund {e}')    
    again = input("Nochmal? 'n' für Abbruch: ")
    if again == 'n':
        break