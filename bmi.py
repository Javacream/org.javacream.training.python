MIN_HEIGHT = 30
MAX_HEIGHT = 250
MIN_WEIGHT = 3
MAX_WEIGHT = 333
while True:

    name = input('Enter your name: ')
    weight = input('Enter your weight: ')
    height = input('Enter your height in cm: ')
    try:
        weight = float(weight)
        height = int(height)
        if weight < MIN_WEIGHT or weight > MAX_WEIGHT:
            print (f'you entered an invalid weight {weight}: must be between {MIN_WEIGHT} and {MAX_WEIGHT}')
        elif height < 30 or weight > 250:
            print (f'you entered an invalid height {height}: must be between {MIN_HEIGHT} and {MAX_HEIGHT}')
        else:
            bmi = weight / (height * height) * 100 * 100 # Berechnung des BMI
            print (f'{name} with weight {weight} and height {height}cm has a body mass index of {bmi:.2f}')
    except:
        print (f'you entered an invalid weight {weight} or height {height}')
        

    again = input ('again? (y|n)')
    if again == 'n':
        break