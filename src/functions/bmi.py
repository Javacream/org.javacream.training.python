def calculate_bmi(weight, height):
    height = height / 100
    bmi = weight / (height**2)
    return bmi

calculated_bmi = calculate_bmi(76.5, 183)
print(f'{calculated_bmi:.2f}')