from bmi import calculate_bmi
from unittest import TestCase, main
class BmiTests(TestCase):
    def test_height_183_and_weight_75_7_calculates_bmi_22_6(self):
        weight = 75.7
        height = 183
        expected_bmi = 22.6
        bmi = calculate_bmi(weight, height)
        self.assertAlmostEqual(expected_bmi, bmi, 1)
    def test_height_177_and_weight_95_7_calculates_bmi_30_5(self):
        weight = 95.7
        height = 177
        expected_bmi = 30.5
        bmi = calculate_bmi(weight, height)
        self.assertAlmostEqual(expected_bmi, bmi, 1)


main()