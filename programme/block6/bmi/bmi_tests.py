import unittest

class BmiTests(unittest.TestCase):

    def test_weight_75_3_and_height_183_calculates_bmi_22_0(self):
        weight = 75.3
        height = 183
        expected_bmi = 22.0
        calculated_bmi = None
        self.assertAlmostEqual(expected_bmi, calculated_bmi, 1)
    def test_bmi_16_is_underweight(self):
        bmi = 16
        expected_category = 'underweight'
        calculated_category = None
        self.assertEqual(expected_category, calculated_category)
    def test_bmi_18_5_is_underweight(self):
        bmi = 18.5
        expected_category = 'underweight'
        calculated_category = None
        self.assertEqual(expected_category, calculated_category)

unittest.main()