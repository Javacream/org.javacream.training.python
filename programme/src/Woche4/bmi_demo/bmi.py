def calculate_bmi(w, h):
    body_mass_index = w/(h**2)*100**2
    return body_mass_index

def main():
    weight = 75.7
    height = 183
    name = "Hugo"
    calculated_bmi = calculate_bmi(weight, height) # Hier wird impliziet w=weight und h=height aufgerufen
    print(calculated_bmi)

    print(calculate_bmi(99.6, 176))

main()