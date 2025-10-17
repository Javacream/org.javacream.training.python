name = input('Bitte Name eingeben: ')
weight = input('Bitte Gewicht in kg eingeben: ')
height = input('Bitte Größe in cm eingeben: ')

weight = float(weight)
height = int(height)
height = height / 100
bmi = weight / (height ** 2)

result = f'{name} hat einen Body Mass Index von {bmi:.2f}'

print(result)