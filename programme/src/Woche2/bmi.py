person_name = input('Bitte geben Sie Ihren Namen an: ')
person_height = input('Bitte geben Sie ihre Körpergröße in Zentimetern an: ')
person_weight = input('Bitte geben Sie ihr Körpergewicht in Kilogramm an, Trennzeichen ist der .: ')
person_height = int(person_height)
person_weight = float(person_weight)
bmi_calculatable = False
person_height_smaller_than_250 = (person_height < 250)
person_height_greater_than_10 = (person_height > 50)
if  person_height_smaller_than_250 and person_height_greater_than_10:
    bmi_calculatable = True
if bmi_calculatable:
    body_mass_index = person_weight / (person_height * person_height) * 100**2
    print(f'Der berechnete BMI für {person_name} ist: {body_mass_index:.2f}')
else:
    print("Mit den Eingaben kann kein sinnvoller BMI berechnet werden!")
