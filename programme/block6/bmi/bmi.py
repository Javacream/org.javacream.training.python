def bmi_calculation(height: int, weight: float) -> float:
    bmi = weight/((height / 100) **2)
    return bmi
def bmi_categorization(bmi: float) -> str:
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 24.9:
        return 'normalweight'
    elif bmi < 30:
        return 'overweight'
    else:
        return 'obese'