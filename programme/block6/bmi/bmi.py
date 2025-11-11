UNDERWEIGHT_LIMIT = 18.5
NORMAL_WEIGHT_LIMIT = 24.9
OVERWEIGHT_LIMIT = 30


def calculate_bmi(weight: float, height: int) -> float:#
    height = height/100
    bmi = weight/(height*height)
    return bmi

def categorize_bmi(bmi: float) -> str:
    if bmi < UNDERWEIGHT_LIMIT:
        return 'underweight'
    elif bmi < NORMAL_WEIGHT_LIMIT:
        return 'normalweight'
    elif bmi < OVERWEIGHT_LIMIT:
        return 'overweight'
    else:
        return 'obese'
    

def main():
    print(calculate_bmi(99.9, 177))

if __name__ == '__main__':
    main()        