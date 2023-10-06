import unittest
import people
class TestSimple(unittest.TestCase):
    def test_simple_ok(self):
        self.assertTrue(True)
    def _test_simple_fail(self):
        self.assertTrue(False)

class TestPeople(unittest.TestCase):
    def test_people_manager(self):
        people_manager = people.people_manager
        people_manager.create("Goo", "Georg")
        people_manager.create("Foo", "Henry")

        search_result = people_manager.find_by_id(0)
        self.assertEqual("Hello, my name is Georg Goo", search_result.info())
        self.assertTrue(people_manager.delete_by_id(0))
        self.assertFalse(people_manager.delete_by_id(0))
        

if __name__ == '__main__':
    unittest.main()