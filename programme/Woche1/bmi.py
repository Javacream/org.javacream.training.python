name = input('Bitte Name eingeben: ')
weight = input('Bitte Körpergewicht eingeben: ')
height = input('Bitte Körpergröße angeben: ')

weight = float(weight)
height = int(height)

bmi = weight/(height*height)*100*100

print(f"Die Person namens {name} hat einen BMI von {bmi}")