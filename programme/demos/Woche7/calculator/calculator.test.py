import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def test_plus(self):
        number1 = 20
        number2 = 22
        expected_sum = 42
        c = Calculator()
        calculated_sum = c.plus(number1, number2)
        self.assertEqual(expected_sum, calculated_sum)
    def test_minus(self):
        number1 = 66
        number2 = 24
        expected_diff = 42
        c = Calculator()
        calculated_diff = c.minus(number1, number2)
        self.assertEqual(expected_diff, calculated_diff)        

if __name__ == '__main__':
    unittest.main()        