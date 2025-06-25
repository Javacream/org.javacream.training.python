MIN_WEIGHT = 3
MAX_WEIGHT = 333
MIN_HEIGHT = 30
MAX_HEIGHT = 250

while True:
    name = input('Enter your name: ')
    weight  = input('Enter your weight in kg: ') 

    weight = float(weight)
    if weight < MIN_WEIGHT or weight > MAX_WEIGHT:
        print(f'you entered an invalid weight: {weight}, must be between {MIN_WEIGHT} and {MAX_WEIGHT}')
    else:    
        height  = input('Enter your height in cm: ') 
        height = int(height)
        if height < MIN_HEIGHT or height > MAX_HEIGHT:
            print(f'you entered an invalid height: {height}, must be between {MIN_HEIGHT} and {MAX_HEIGHT}')
        else:
            height = height / 100 
            bmi = weight / (height * height) 
            print(f'{name} has a body mass index of {bmi:.2f}')
    again = input('Again? y|n: ')
    if again == 'n':
        break