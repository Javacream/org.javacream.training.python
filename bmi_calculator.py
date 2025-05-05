name = input("Bitte Name eingeben: ")
weight = input("Bitte Körpergewicht in kg: ")
height = input("Bitte Körpergröße in Meter: ")
weight = float(weight)
height = float(height)
body_mass_index = weight/(height**2)

is_underweighted = body_mass_index < 18
is_normalweighted = body_mass_index >= 18 and body_mass_index <= 22
is_overweighted = body_mass_index > 22 and body_mass_index <25

if is_underweighted:
    print(f'{name} ist untergewichtig')
elif is_normalweighted:
    print(f'{name} ist normalgewichtig')
elif is_overweighted:
    print(f'{name} ist übergewichtig')
else:
    print(f'{name} ist fettleibig')
