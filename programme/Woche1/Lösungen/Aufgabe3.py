# Dieses Programm berechnet den BMI einer Person
name=input('Bitte geben Sie ihren Namen ein: ')
height=input('Bitte geben Sie ihre Körpergröße in Zentimetern ein: ')
weight=input('Bitte geben Sie ihr Gewicht mit einer Nachkommastelle ein (Hinweis: Trennzeichen muss der Punkt sein!): ')
height = int(height)
weight = float(weight)
bmi=weight/(height*height)*10000
message = f'Die Person namens {name} hat einen BMI von {bmi:.2f}'
print(message)