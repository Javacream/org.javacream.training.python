while True:
    name = input('Please enter your name: ')
    try:
        weight = input(f'{name}, please enter your weight in kg: ')
        weight = float(weight) 
        try:
            height = input(f'{name}, please enter your height in cm: ')
            height = int(height)
            height = height / 100
            bmi = weight / (height**2)
            if bmi < 18.5:
                bmi_category = 'underweight'
            elif bmi < 25:
                bmi_category = 'normalweight'
            elif bmi < 30:
                bmi_category = 'overweight'
            else:
                bmi_category = 'obese'
            print(f'{name} with weight {weight} and height {height} has a bmi of {bmi:.2f} and is therefor {bmi_category}')
        except:
            print(f'{name} entered a wrong height: {height}')        
    except:
        print(f'{name} entered a wrong weight: {weight}')
    again = input ('new calculation (y|n)? ')
    if 'y' == again:
        pass
    else:
        break