'''
Ablauf eines Testes
1. Definiere Eingangsdaten (Größe: 183, Gewicht 75.3)
2. Definiere das erwartete Ergebnis (-> Andere Quelle, z.B. aus der Fachvorgabe, BMI 22.485)
3. Rufe den zu testenden Algorithmus auf und merke dir das berechnete Ergebnis
4. Formuliere Annahmen / Assertions: 'Das erwartete Ergebnis ist gleich dem berechneten Ergebnis'
'''
from bmi_calculator import calculate_bmi
import unittest

class BmiCalculatorTests(unittest.TestCase):
    def test_bmi_calculation_with_valid_height_and_weight(self):
        height = 183
        weight = 75.3
        expected_bmi = 22.485
        calculated_bmi = calculate_bmi(height, weight)
        self.assertAlmostEqual(expected_bmi, calculated_bmi, 5)
    def test_bmi_calculation_fails_if_height_lt_50(self):
        height = 45
        weight = 75.3
        result = calculate_bmi(height, weight)
        self.assertFalse(result)
    def test_bmi_calculation_fails_if_weight_lt_0(self):
        height = 183
        weight = -5
        result = calculate_bmi(height, weight)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()