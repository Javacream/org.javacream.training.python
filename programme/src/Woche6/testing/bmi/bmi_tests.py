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
    def test_height_49_must_raise_an_error(self):
        weight = 95.7
        height = 49
        ok = True
        try:
            calculate_bmi(weight, height)
            ok = False
        except:
            pass
        self.assertTrue(ok)
    def test_height_251_must_raise_an_error(self):
        weight = 95.7
        height = 251
        ok = True
        try:
            calculate_bmi(weight, height)
            ok = False
        except:
            pass
        self.assertTrue(ok)
    def test_weight_1_9_must_raise_an_error(self):
        weight = 1.9
        height = 183
        ok = True
        try:
            calculate_bmi(weight, height)
            ok = False
        except:
            pass
        self.assertTrue(ok)
    def test_weight_450_1_must_raise_an_error(self):
        weight = 450.1
        height = 183
        ok = True
        try:
            calculate_bmi(weight, height)
            ok = False
        except:
            pass
        self.assertTrue(ok)
    def test_weight_35_and_height_199_must_raise_an_error(self):
        weight = 35
        height = 199
        ok = True
        try:
            calculate_bmi(weight, height)
            ok = False
        except:
            pass
        self.assertTrue(ok)
    def test_weight_100_and_height_51_must_raise_an_error(self):
        weight = 100
        height = 51
        ok = True
        try:
            calculate_bmi(weight, height)
            ok = False
        except:
            pass
        self.assertTrue(ok)

main()