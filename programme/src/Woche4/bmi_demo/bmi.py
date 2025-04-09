def calculate_bmi(**person_data):
    weight = person_data["w"]
    height = person_data["h"]
    body_mass_index = weight/(height**2)*100**2
    return body_mass_index

def main():
    weight = 75.7
    height = 183
    calculated_bmi = calculate_bmi(w=weight, h=height) # Hier wird impliziet w=weight und h=height aufgerufen
    print(calculated_bmi)

main()