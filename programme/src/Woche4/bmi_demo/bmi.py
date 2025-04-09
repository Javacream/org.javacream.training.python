def calculate_bmi(weight, height):
    body_mass_index = weight/(height**2)*100**2
    return body_mass_index


weight = 75.7
height = 183

calculated_bmi = calculate_bmi(weight, height)
print(calculated_bmi)

print(calculate_bmi(99.6, 176))