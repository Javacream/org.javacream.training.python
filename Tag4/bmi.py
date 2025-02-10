def calculate_bmi(height, weight):
    bmi = weight / (height*height) * 10000
    return bmi

MAX_HEALTHY_BMI = 25