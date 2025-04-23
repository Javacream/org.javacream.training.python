def calculate_bmi(weight, height):
    if height < 50:
        raise Exception(f'invalid height: {height}')
    body_mass_index = weight/(height**2)*100**2
    return body_mass_index
