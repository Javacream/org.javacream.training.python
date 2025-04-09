def calculate_bmi(**person_data):
    weight = person_data["w"]
    height = person_data["h"]
    body_mass_index = weight/(height**2)*100**2
    return body_mass_index
def get_height():
    person_height = input('Bitte geben Sie ihre Körpergröße in Zentimetern an: ')
    person_height = int(person_height)
    return person_height

def main():
    weight = 75.7
    height = get_height()
    calculated_bmi = calculate_bmi(w=weight, h=height) # Hier wird impliziet w=weight und h=height aufgerufen
    print(calculated_bmi)

main()