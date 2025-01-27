name = input('Bitte geben Sie ihren Namen an: ')
height = input('Bitte geben Sie ihre Körpergröße in cm an (Nur Zahlen!): ')
weight = input('Bitte geben Sie ihr Körpergewicht in kg an (Nur Zahlen, Komma-Trenner ist der Punkt .): ')
height = int(height)
weight = float(weight)
body_mass_index = weight/(height*height)* 100 * 100
print(f'Die Person {name} hat mit einer Körpergröße von {height}cm und einem Gewicht von {weight}kg einen BMI von {body_mass_index}')