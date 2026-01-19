def get_name():
    pass

def get_height():
    pass

def get_weight():
    pass

def calculate_bmi(height, weight):
    pass

def calculate_bmi_category(bmi):
    pass

def calculate_result_text(name, height, weight, bmi_category):
    pass

def main():
    name = get_name()
    height = get_height()
    weight = get_weight()
    bmi = calculate_bmi(height, weight)
    bmi_category = calculate_bmi_category(bmi)
    result = calculate_result_text(name, height, weight, bmi_category)
    print(result)

main()