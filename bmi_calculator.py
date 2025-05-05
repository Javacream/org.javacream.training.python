UNDERWEIGHT_LIMIT = 18
NORMALWEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30
name = input("Bitte Name eingeben: ")
weight = input("Bitte Körpergewicht in kg: ")
height = input("Bitte Körpergröße in Meter: ")
weight = float(weight)
height = float(height)
body_mass_index = weight/(height**2)

if body_mass_index < UNDERWEIGHT_LIMIT:
    print(f'{name} ist untergewichtig')
elif body_mass_index >= UNDERWEIGHT_LIMIT and body_mass_index <= NORMALWEIGHT_LIMIT:
    print(f'{name} ist normalgewichtig')
elif body_mass_index > NORMALWEIGHT_LIMIT and body_mass_index < OVERWEIGHT_LIMIT:
    print(f'{name} ist übergewichtig')
else:
    print(f'{name} ist fettleibig')
