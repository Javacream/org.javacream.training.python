import bmi
def main():
    person_data = [
        [183, 75.6],
        [176, 88.8],
        [166, 66.6]
    ]
    for person in person_data:
        bmi_result = bmi.calculate_bmi(person[0], person[1])
        print(bmi_result)

main()

