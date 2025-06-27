import unittest
import shopping_list_module as slm
class ShoppingListModuleTests(unittest.TestCase):
    def test_create_shopping_list(self):
        rows = ['X:egg', 'X:apple', 'X:egg']
        expected_row1 = 'egg=2\n'
        expected_row2 = 'apple=1\n'
        result = slm.create_shopping_list(rows)
        self.assertIn(expected_row1, result)
        self.assertIn(expected_row2, result)
    def test_calculate_number_of_people(self):
        rows = ['X:egg', 'Y:apple', 'X:egg']
        expected_number_of_people = 2
        result = slm.calculate_number_of_people(rows)
        self.assertEqual(expected_number_of_people, result)


if __name__ == '__main__':
    unittest.main()