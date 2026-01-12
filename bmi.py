name = input('Please enter your name: ')
try:
    weight = input(f'{name}, please enter your weight in kg: ')
    weight = float(weight) 
    try:
        height = input(f'{name}, please enter your height in cm: ')
        height = int(height)
        height = height / 100
        bmi = weight / (height**2)
        print(f'{name} with weight {weight} and height {height} has a bmi of {bmi:.2f}')
    except:
        print(f'{name} entered a wrong height: {height}')        
except:
    print(f'{name} entered a wrong weight: {weight}')