import unittest
import bmi_calculator

class BmiCalculatorTests(unittest.TestCase):
    def test_bmi_calculator_is_available(self):
        self.assertIsNotNone(bmi_calculator.calculate_bmi)

    def test_height_183_and_weight_75_calculates_bmi_22_3954(self):
        HEIGHT = 1.83
        WEIGHT = 75
        EXPECTED_BMI = 22.3954
        calculated_bmi = bmi_calculator.calculate_bmi(HEIGHT, WEIGHT)
        self.assertAlmostEqual(EXPECTED_BMI, calculated_bmi, None, "Not Equal", 0.001)
unittest.main()