def calculate_bmi(height, weight):
    bmi = weight / (height*height) * 10000
    return bmi

def main():
    person_data = [
        [183, 75.6],
        [176, 88.8],
        [166, 66.6]
    ]
    for person in person_data:
        bmi = calculate_bmi(person[0], person[1])
        print(bmi)

main()

