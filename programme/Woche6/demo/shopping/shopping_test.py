import unittest
import file_util
import shopping

class FileUtilTests(unittest.TestCase):
    def test_read_raw(self):
        self.fail('ToDo')
    def test_clean_data(self):
        self.fail('ToDo')
    def test_write_result(self):
        self.fail('ToDo')
class ShoppingTests(unittest.TestCase):
    def test_create_unique_items(self):
        items_list = ['A', 'B', 'C', 'B', 'D', 'A', 'A']
        expected_item_set = {'A', 'B', 'C', 'D'}
        
        calculated_item_set = shopping.create_unique_items(items_list)

        self.assertEqual(expected_item_set, calculated_item_set)
    def test_create_shopping_collection(self):
        self.fail('ToDo')


if __name__ == '__main__':
    unittest.main()