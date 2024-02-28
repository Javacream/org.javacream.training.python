import unittest
import greetings

class TestGreeting(unittest.TestCase):
    def test_greet_creates_greeting(self):
        name ="Sawitzki"
        expected_greeting = "Hello Sawitzki!"
        greeting = greetings.greet(name)
        self.assertEqual(expected_greeting, greeting)

unittest.main()