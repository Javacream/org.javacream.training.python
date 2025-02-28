LOW_WEIGHT_BMI = 18
MAX_NORMAL_BMI = 25
MAX_HIGH_WEIGHT_BMI = 30
while True:
    name = input('please enter your name: ')
    height = input('please enter your height in cm (numbers only!): ')
    weight = input('please enter your weight in kg(numbers and one . only): ')
    try:
        height = int(height)
        weight = float(weight)
        body_mass_index = weight/(height*height)* 100 * 100
        if body_mass_index < LOW_WEIGHT_BMI:
            bmi_category = 'underweight'
        elif body_mass_index < MAX_NORMAL_BMI:
            bmi_category = 'normalweight'    
        elif body_mass_index < MAX_HIGH_WEIGHT_BMI:
            bmi_category = 'overweight'    
        else:
            bmi_category = "obese"
        print(f'{name} with a height of {height}cm and weight of {weight}kg has a BMI of {body_mass_index:.2f} and is {bmi_category}')
    except:
        print(f'your input for height(you entered {height}) or weight(you entered {weight}) cannot be interpreted as a number')    
    again = input("again? 'x' for exit: ")
    if again == 'x':
        break
