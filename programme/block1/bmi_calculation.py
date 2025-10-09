weight = input('Bitte geben Sie Ihr Körpergewicht in kg ein: ')
height = input('Bitte geben Sie Ihre Größe in cm an: ')
weight = float(weight)
height = int(height)
height = height / 100
bmi = weight/(height**2)

result = f'Berechnete BMI ist {bmi:.2f}'
print(result)