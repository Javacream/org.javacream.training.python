import bmi_services
def main():
    input_path = 'src/applications/bmi/people.csv'
    result_path = 'src/applications/bmi/bmi.txt'
    people_data = bmi_services.read_people_data(input_path)
    for raw_person_data in people_data:
        name, height, weight = bmi_services.extract(raw_person_data)
        bmi = bmi_services.calculate_bmi(height, weight)
        bmi_category = bmi_services.calculate_bmi_category(bmi)
        result = bmi_services.calculate_result_text(name, height, weight, bmi, bmi_category)
        bmi_services.write(result_path, result)

main()