try:
    number1 = input("Bitte eine Zahl eingeben (Kommazeichen ist der Punkt!): ")
    number1 = float(number1)
    number2 = input("Bitte eine Zahl eingeben (Kommazeichen ist der Punkt!): ")
    number2 = float(number2)
    print(f"{number1} + {number2} = {number1 + number2}")
    print(f"{number1} - {number2} = {number1 - number2}")
    print(f"{number1} * {number2} = {number1 * number2}")
    print(f"{number1} / {number2} = {number1 / number2}")
except:
    print(f"du hast leider mindestens eine ungültige Zahl eingegeben: {number1}, {number2}")
