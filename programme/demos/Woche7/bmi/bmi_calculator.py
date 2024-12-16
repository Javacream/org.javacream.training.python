def calculate_bmi(height, weight):
    if height < 30 or height > 275:
        raise Exception()
    bmi = weight / (height * height) * 100 * 100
    return bmi