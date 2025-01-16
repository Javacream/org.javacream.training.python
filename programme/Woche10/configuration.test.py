import unittest
from configuration import read_configuration

class ConfigurationTest(unittest.TestCase):
    def test_read_configuration(self):
        configuration = read_configuration('programme/Woche10/configuration.json')
        self.assertEqual(3, len(configuration))

if __name__ == '__main__':
    unittest.main()