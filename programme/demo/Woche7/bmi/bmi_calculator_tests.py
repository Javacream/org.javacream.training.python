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
    def test_bmi_calculation(self):
        height = 183
        weight = 75.3
        expected_bmi = 22.485
        calculated_bmi = calculate_bmi(height, weight)
        self.assertAlmostEqual(expected_bmi, calculated_bmi, 5)
if __name__ == '__main__':
    unittest.main()