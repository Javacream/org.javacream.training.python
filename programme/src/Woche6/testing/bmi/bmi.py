def calculate_bmi(weight, height):
    if (height < 50) or (height > 250) :
        raise Exception(f'invalid height: {height}')
    if (weight < 2) or (weight > 450) :
        raise Exception(f'invalid weight: {weight}')
    body_mass_index = weight/(height**2)*100**2
    if (body_mass_index < 10) or (body_mass_index > 50):
        raise Exception(f'invalid bmi: {body_mass_index}')
    return body_mass_index
