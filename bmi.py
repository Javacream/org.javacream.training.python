name = input('Bitte geben Sie ihren Namen an: ')
height = input('Bitte geben Sie ihre Körpergröße in cm an (Nur Zahlen!): ')
weight = input('Bitte geben Sie ihr Körpergewicht in kg an (Nur Zahlen, Komma-Trenner ist der Punkt .): ')
height = int(height)
weight = float(weight)
body_mass_index = weight/(height*height)* 100 * 100
if body_mass_index < 18:
    bmi_category = 'untergewichtig'
elif body_mass_index < 25:
    bmi_category = 'normalgewichtig'    
elif body_mass_index < 30:
    bmi_category = 'übergewichtig'    
else:
    bmi_category = "fettleibig"
print(f'Die Person {name} hat mit einer Körpergröße von {height}cm und einem Gewicht von {weight}kg einen BMI von {body_mass_index} ist {bmi_category}')