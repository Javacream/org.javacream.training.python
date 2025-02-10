import bmi as bmi_module 
def main():
    person_data = [
        [183, 75.6],
        [176, 88.8],
        [166, 66.6]
    ]
    for person in person_data:
        bmi = bmi_module.calculate_bmi(person[0], person[1])
        print(bmi)

main()

