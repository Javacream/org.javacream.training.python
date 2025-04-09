def calculate_bmi(*people_data):
    weight = people_data[0]
    height = people_data[1]
    body_mass_index = weight/(height**2)*100**2
    return body_mass_index

def main():
    weight = 75.7
    height = 183
    calculated_bmi = calculate_bmi(weight, height) # Hier wird impliziet w=weight und h=height aufgerufen
    print(calculated_bmi)
    calculated_bmi = calculate_bmi(weight, height, True, 42, "Hugo") # Hier wird impliziet w=weight und h=height aufgerufen

main()