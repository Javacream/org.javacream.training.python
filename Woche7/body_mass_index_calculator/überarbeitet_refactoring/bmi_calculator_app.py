import bmi_calculator

def main():
    name = input("Bitte Namen eingeben: ")
    weight = input (f"Bitte Körpergewicht in kg zwischen {bmi_calculator.MIN_WEIGHT} und {bmi_calculator.MAX_WEIGHT} eingeben: ")
    height = input (f"Bitte Körpergröße in m zwischen {bmi_calculator.MIN_HEIGHT} und {bmi_calculator.MAX_HEIGHT} eingeben: ")
    try:
        weight = float(weight)
        height = float(height)
        try:
            bmi = bmi_calculator.calculate_bmi(height, weight)
            print(f"Name: {name} mit Gewicht: {weight} und Größe {height} hat einen BMI von {bmi}") # Format-String
        except:
            print(f"Ungültiger Bereich für Gewicht oder Körpergröße: {weight}, {height}")    

    except:
        print(f"Fehler, Gewicht {weight} oder Größe {height} können  nicht als Zahl interpretiert werden")

    print("Fertig")
main()