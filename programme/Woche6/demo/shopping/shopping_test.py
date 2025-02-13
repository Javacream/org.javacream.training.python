import unittest
import file_util
import shopping

import os
class JavacreamTestCase(unittest.TestCase):
    def assertFileExists(self, path):
        if not os.path.isfile(path):
            self.fail(f"File {path} does not exist")
class FileUtilTests(JavacreamTestCase):
    def test_read_raw(self):
        path = 'programme/Woche6/demo/shopping/test_data.txt'
        
        expected_number_of_lines = 10
        expected_row_3 = 'Test\n'
        rows = file_util.read_raw(path)
        self.assertEqual(expected_number_of_lines, len(rows))
        self.assertEqual(expected_row_3, rows[2])

    def test_clean_data(self):
        self.fail('ToDo')
    def test_write_result(self):
        items_list = ['A', 'B', 'C', 'B', 'D', 'A', 'A']
        path = 'programme/Woche6/demo/shopping/test_written.txt'

        file_util.write_result(items_list, path)
        # ich finde keine Standard-Assertion
        self.assertFileExists(path)
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