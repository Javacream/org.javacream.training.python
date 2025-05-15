def calculate_bmi(weight_parameter, height_parameter):
    body_mass_index = weight_parameter/(height_parameter**2)
    return body_mass_index

def main():
    weight = float(input("Bitte Gewicht eingeben:"))
    height = float(input("Bitte Größe eingeben:"))
    bmi = calculate_bmi(76.6, 1.83) # Implizit: weight_parameter = 76.6 height_parameter=1.83
    bmi = calculate_bmi(weight, height) # Implizit: weight_parameter = weight height_parameter=height
    print(bmi)

main()