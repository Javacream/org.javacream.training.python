def calculate_bmi(weight: float, height: int) -> float:#
    height = height/100
    bmi = weight/(height*height)
    return bmi

def categorize_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 24.9:
        return 'normalweight'
    elif bmi < 30:
        return 'overweight'
    else:
        return 'obese'
    

def main():
    print(calculate_bmi(99.9, 177))

if __name__ == '__main__':
    main()        