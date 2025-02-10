from bmi import calculate_bmi as cbmi, MAX_HEALTHY_BMI as MHB
def main():
    person_data = [
        [183, 75.6],
        [176, 88.8],
        [166, 66.6]
    ]
    for person in person_data:
        bmi = cbmi(person[0], person[1])
        print(bmi)
    print(MHB)

main()

