UNDERWEIGHT_BMI = 18
MAX_NORMAL_BMI = 25
MAX_FAT_BMI = 30

def calculate_bmi(height, weight):
    bmi = weight / (height * height) # height in Metern, nicht wie bisher in cm
    return bmi

def bmi_category_for(bmi):
    if bmi < UNDERWEIGHT_BMI:
        return 'untergewichtig'
    elif bmi < MAX_NORMAL_BMI:
        return 'normalgewichtig'
    elif bmi < MAX_FAT_BMI:
        return 'übergewichtig'
    else:
        return 'fettleibig'
