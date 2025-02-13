import unittest
import file_util
import shopping

import os
class JavacreamTestCase(unittest.TestCase):
    def delete_file(self, path):
        if os.path.isfile(path):
            os.remove(path)
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
        dirty_data = ['a\n', '\n', 'Test\n', '\n', 'End']
        expected_cleaned_data = ['a', 'Test', 'End']

        calculated_cleaned_data = file_util.clean_data(dirty_data)

        self.assertEqual(expected_cleaned_data, calculated_cleaned_data)
    def test_write_result(self):
        items_list = ['A', 'B', 'C', 'B', 'D', 'A', 'A']
        path = 'programme/Woche6/demo/shopping/test_written.txt'
        self.delete_file(path)
        file_util.write_result(items_list, path)
        self.assertFileExists(path)
        self.delete_file(path)
class ShoppingTests(unittest.TestCase):
    def test_create_unique_items(self):
        items_list = ['A', 'B', 'C', 'B', 'D', 'A', 'A']
        expected_item_set = {'A', 'B', 'C', 'D'}
        
        calculated_item_set = shopping.create_unique_items(items_list)

        self.assertEqual(expected_item_set, calculated_item_set)
    def test_create_shopping_collection(self):
        items_list = ['A', 'B', 'C', 'B', 'D', 'A', 'A']
        expected_list = ['A -> 3', 'B -> 2', 'C -> 1', 'D -> 1']

        calculated_list = shopping.create_shopping_collection(items_list)

        self.assertEqual(expected_list, calculated_list)

if __name__ == '__main__':
    unittest.main()