underweight_limit = 18.5
normalweight_limit = 24.9
overweight_limit = 30


def bmi_calculation(height: int, weight: float) -> float:
    bmi = weight/((height / 100) **2)
    return bmi
def bmi_categorization(bmi: float) -> str:
    if bmi < underweight_limit:
        return 'underweight'
    elif bmi < normalweight_limit:
        return 'normalweight'
    elif bmi < overweight_limit:
        return 'overweight'
    else:
        return 'obese'