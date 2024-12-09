import unittest
from bmi_calculator import calculate_bmi
class BmiCalculatorTest(unittest.TestCase):
    def test_bmi_calculator(self):
        # Definition der Eingangsdaten
        height = 183
        weight = 75.3
        # Erwartetes Resultat
        expected_bmi = 22.485
        # Aufruf des zu testenden Algorithmus mit den Eingangsdaten 
        bmi = calculate_bmi(height, weight)
        # Prüfen von Assertions / Annahmen
        self.assertAlmostEqual(expected_bmi, bmi, 5)
if __name__ == '__main__':
    unittest.main()