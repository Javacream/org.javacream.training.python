import unittest
from setup_utilities import *

class UtilitiesTest(unittest.TestCase):
    def test_create_names(self):
        people = [
            {
                "id": 1,
                "lastname": "Sawitzki",
                "firstname": "Rainer",
                "gender": "m",
                "height": 183
            },
            {
                "id": 2,
                "lastname": "Meier",
                "firstname": "Hans",
                "gender": "m",
                "height": 163
            },
            {
                "id": 3,
                "lastname": "Metzger",
                "firstname": "Georg",
                "gender": "m",
                "height": 190
            }
        ]

        self.assertEqual(['Rainer.Sawitzki', 'Hans.Meier', 'Georg.Metzger'], names_from_people_list(people))
    def test_directories(self):
        result = directories_from_path('p1/p2/p3')
        self.assertEqual(['p1', 'p1/p2', 'p1/p2/p3'], result)
if __name__ == '__main__':
    unittest.main()