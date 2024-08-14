NEW_CALCULATION_INPUT_MESSAGE = "soll eine neue Berechung durchgeführt werden (J / n):"
NAME_INPUT_MESSAGE = "Bitte geben Sie Ihren Namen an: "
MAX_HEIGHT = 250
MIN_HEIGHT = 50
HEIGHT_INPUT_MESSAGE = f"Bitte geben Sie Ihre Körpergröße zwischen {MIN_HEIGHT} und {MAX_HEIGHT} in Zentimetern an: "
MAX_WEIGHT = 500
MIN_WEIGHT = 3
WEIGHT_INPUT_MESSAGE = f"Bitte geben Sie Ihr Körpergewicht zwischen {MIN_WEIGHT} und {MAX_WEIGHT} in Kilogramm an: "
UNDERWEIGHT_BMI_LIMIT = 18
OVERWEIGHT_BMI_LIMIT = 25
FATWEIGHT_BMI_LIMIT = 30
UNDERWEIGHT_MESSAGE = "untergewichtig"
NORMALWEIGHT_MESSAGE = "normalgewichtig"
OVERWEIGHT_MESSAGE = "übergewichtig"
FATWEIGHT_MESSAGE = "fettleibig"

while True:
    name = input(NAME_INPUT_MESSAGE)
    height = input(HEIGHT_INPUT_MESSAGE)
    weight = input(WEIGHT_INPUT_MESSAGE)
    try:
        height = int(height)
        weight = float(weight)
        if height < MIN_HEIGHT or height > MAX_HEIGHT:
            print(f"ungültige Körpergröße: {height}")
            continue
        if weight < MIN_WEIGHT or height > MAX_WEIGHT:
            print(f"ungültiges Körpergewicht: {weight}")
            continue

        bmi = weight /  ((height/100) * (height/100))
        if bmi < UNDERWEIGHT_BMI_LIMIT:
            bmi_message = UNDERWEIGHT_MESSAGE
        elif bmi < OVERWEIGHT_BMI_LIMIT:
            bmi_message = NORMALWEIGHT_MESSAGE
        elif bmi < FATWEIGHT_BMI_LIMIT:
            bmi_message = OVERWEIGHT_MESSAGE
        else:
            bmi_message = FATWEIGHT_MESSAGE
        print(f'{name} ist mit einem bmi von {bmi} {bmi_message}')

        new_calculation = input(NEW_CALCULATION_INPUT_MESSAGE)
        if new_calculation == 'n':
            break
    except:
        print(f"ungültige Eingabe von Gewicht {weight} und / oder Körpergröße: {height}")