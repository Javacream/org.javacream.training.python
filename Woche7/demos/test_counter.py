import unittest
import counter

class ApplicationTest(unittest.TestCase):
    def test_instantiation(self):
        actual_counter = counter.Counter()
        self.assertIsNotNone(actual_counter)
    def test_counter_is_set_to_zero(self):
        actual_counter = counter.Counter()
        self.assertEqual(0, actual_counter.counter)
    def test_counter_is_set_to_one(self):
        actual_counter = counter.Counter()
        actual_counter.increment()
        self.assertEqual(1, actual_counter.counter)

unittest.main()