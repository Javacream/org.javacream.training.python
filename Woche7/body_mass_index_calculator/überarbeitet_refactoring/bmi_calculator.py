# Functional

def calculate_bmi(height, weight):
    MIN_WEIGHT = 0.5
    MAX_WEIGHT = 333
    MIN_HEIGHT = 0.25
    MAX_HEIGHT = 2.5
    valid = False
    if weight >= MIN_WEIGHT and weight <= MAX_WEIGHT:
        if height >= MIN_HEIGHT and height <= MAX_HEIGHT:
            bmi = weight / ( height * height ) 
            valid = True
    if valid:
        return bmi
    else:
        #return -1 # Signalisiert, dass ein height oder weight nicht korrekt übergeben wurde
        raise Exception(f"Ungültiger Bereich für Gewicht [{MIN_WEIGHT} - {MAX_WEIGHT}] oder Körpergröße [{MIN_HEIGHT} - {MAX_HEIGHT}]: {weight}, {height}")
# OOP

class BmiCalculator:
    def calculate_bmi(self, height, weight):
        pass
