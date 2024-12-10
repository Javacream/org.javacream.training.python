def calculate_bmi(height, weight):
    if height < 50:
        return False
    if weight <= 0:
        return False
    bmi = weight/(height*height)*100*100
    return bmi