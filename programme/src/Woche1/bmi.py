person_name = input('Bitte geben Sie Ihren Namen an: ')
person_height = input('Bitte geben Sie ihre Körpergröße in Zentimetern an: ')
person_weight = input('Bitte geben Sie ihr Körpergewicht in Kilogramm an, Trennzeichen ist der .: ')
person_height = int(person_height)
person_weight = float(person_weight)
body_mass_index = person_weight / (person_height * person_height) * 100**2
print(f'Der berechnete BMI für {person_name} ist: {body_mass_index:.2f}')