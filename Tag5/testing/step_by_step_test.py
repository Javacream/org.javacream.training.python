import unittest

class ListTests(unittest.TestCase):
    def test_list_append(self):
        value = "Hello"
        expected_length_of_list = 1
        my_list = []
        my_list.append(value)
        self.assertEqual(expected_length_of_list, len(my_list)) 

if __name__ == '__main__':
    unittest.main()