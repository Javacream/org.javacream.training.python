import unittest
from bmi import bmi_calculation, bmi_categorization
class BmiTests(unittest.TestCase):
    def test_weight_of_75_and_height_of_185_has_bmi_of_22(self):
        weight = 75.3
        height = 185
        expected_bmi = 22.0

        calculated_bmi = bmi_calculation(height, weight)

        self.assertAlmostEqual(expected_bmi, calculated_bmi, 1)
        
    def test_bmi_of_16_has_category_underweight(self):
        bmi = 16
        expected_category = 'underweight'
        calculated_category = bmi_categorization(bmi)
        self.assertEqual(expected_category, calculated_category)
    def test_bmi_of_33_has_category_obese(self):
        bmi = 33
        expected_category = 'obese'
        calculated_category = bmi_categorization(bmi)
        self.assertEqual(expected_category, calculated_category)

unittest.main()