class BmiCalculator:
    def calculate_bmi(self, weight, height):
        bmi = weight/(height/100)**2
        return bmi