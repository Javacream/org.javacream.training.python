while True:
    name = input('Enter your name: ')
    weight  = input('Enter your weight in kg: ') 

    weight = float(weight)
    if weight < 3 or weight > 333:
        print(f'you entered an invalid weight: {weight}, must be between 3 and 333')
    else:    
        height  = input('Enter your height in cm: ') 
        height = int(height)
        if height < 30 or height > 250:
            print(f'you entered an invalid height: {height}, must be between 30 and 250')
        else:
            height = height / 100 
            bmi = weight / (height * height) 
            print(f'{name} has a body mass index of {bmi:.2f}')
    again = input('Again? y|n: ')
    if again == 'n':
        break