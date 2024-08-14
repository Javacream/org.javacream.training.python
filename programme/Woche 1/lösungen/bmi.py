name = input("Bitte geben Sie Ihren Namen an: ")
height = input("Bitte geben Sie Ihre Körpergröße in Zentimetern an: ")# height ist ein str
weight = input("Bitte geben Sie Ihr Körpergewicht in Kilogramm an: ")# weight ist ein str

# Typ-Umwandlung
height = int(height) # ab jetzt ist height ein int
weight = float(weight) # ab jetzt ist height ein int

bmi = weight /  ((height/100) * (height/100))
print(f'{name} hat einen BMI von {bmi}')
