MAX_HEIGHT = 250
MIN_HEIGHT = 50
MIN_WEIGHT = 2
MAX_WEIGHT = 450
MIN_BMI = 10
MAX_BMI = 40
while True:
    try:
        person_name = input('Bitte geben Sie Ihren Namen an bzw. <Enter> für Programmende: ')
        if person_name != "":
            person_height = input('Bitte geben Sie ihre Körpergröße in Zentimetern an: ')
            person_height = int(person_height)
            height_is_valid =  (person_height < MAX_HEIGHT) and (person_height > MIN_HEIGHT)
            if height_is_valid:
                person_weight = input('Bitte geben Sie ihr Körpergewicht in Kilogramm an, Trennzeichen ist der .: ')
                person_weight = float(person_weight)
                weight_is_valid =  (person_weight < MAX_WEIGHT) and (person_weight > MIN_WEIGHT)
                if weight_is_valid:
                    body_mass_index = person_weight / (person_height * person_height) * 100**2
                    bmi_is_valid = (body_mass_index < MAX_BMI) and (body_mass_index > MIN_BMI)
                    if bmi_is_valid:
                        print(f'Der berechnete BMI für {person_name} ist: {body_mass_index:.2f}')
                    else:
                        print(f"Eingaben prüfen! Der mit Körpergröße {person_height} und -gewicht {person_weight} berechnete BMI {body_mass_index:.2f} fällt außerhalb des möglichen Bereichs {MIN_BMI} bis {MAX_BMI}")
                else:
                    print(f"Sie müssen ein Körpergewicht zwischen zwischen {MIN_WEIGHT} und {MAX_WEIGHT} angegeben, Ihre Eingabe war {person_weight}")
            else:
                print(f"Sie müssen eine Körpergröße zwischen zwischen {MIN_HEIGHT} und {MAX_HEIGHT} angegeben, Ihre Eingabe war {person_height}")
        else:
            break
    except Exception as e:
        print(f"Fehler {e}, versuchs nochmal...")