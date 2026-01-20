from bmi_services import read_people_data, extract, calculate_bmi, calculate_result_text, calculate_bmi_category, write
def main():
    input_path = 'src/applications/bmi/people.csv'
    result_path = 'src/applications/bmi/bmi.txt'
    people_data = read_people_data(input_path)
    for raw_person_data in people_data:
        name, height, weight = extract(raw_person_data)
        bmi = calculate_bmi(height, weight)
        bmi_category = calculate_bmi_category(bmi)
        result = calculate_result_text(name, height, weight, bmi, bmi_category)
        write(result_path, result)

main()