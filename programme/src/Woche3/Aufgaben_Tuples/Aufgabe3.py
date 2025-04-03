seasons = ('Frühling', 'Sommer', 'Herbst', 'Winter')

season = input("Geben Sie eine Jahreszeit an: ")

if season in seasons:
    print(f'{season} ist eine Jahreszeit')
else:
    print(f'{season} ist keine Jahreszeit')