LOW_WEIGHT_BMI = 18
MAX_NORMAL_BMI = 25
MAX_HIGH_WEIGHT_BMI = 30
name = input('Bitte geben Sie ihren Namen an: ')
height = input('Bitte geben Sie ihre Körpergröße in cm an (Nur Zahlen!): ')
weight = input('Bitte geben Sie ihr Körpergewicht in kg an (Nur Zahlen, Komma-Trenner ist der Punkt .): ')
height = int(height)
weight = float(weight)
body_mass_index = weight/(height*height)* 100 * 100
if body_mass_index < LOW_WEIGHT_BMI:
    bmi_category = 'untergewichtig'
elif body_mass_index < MAX_NORMAL_BMI:
    bmi_category = 'normalgewichtig'    
elif body_mass_index < MAX_HIGH_WEIGHT_BMI:
    bmi_category = 'übergewichtig'    
else:
    bmi_category = "fettleibig"
print(f'Die Person {name} hat mit einer Körpergröße von {height}cm und einem Gewicht von {weight}kg einen BMI von {body_mass_index} ist {bmi_category}')