import unittest
from bmi_calculator import BmiCalculator
class BmiCalculatorTests(unittest.TestCase):
    def test_bmi_calculation(self):
        weight = 76.6
        height = 183
        expected_bmi = 22.9
        bmi_calculator = BmiCalculator()
        calculated_bmi = bmi_calculator.calculate_bmi(weight, height)
        self.assertAlmostEqual(expected_bmi, calculated_bmi, 1)
    def test_demo(self):
        name = "Sawitzki"
        expected_name = "SAWITZKI"
        calculated_name = name.lower()
        self.assertEqual(expected_name, calculated_name)
if __name__ == '__main__':
    unittest.main()