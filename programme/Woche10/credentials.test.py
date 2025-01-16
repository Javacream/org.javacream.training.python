import unittest
from credentials import get_password

class CredentialTest(unittest.TestCase):
    def test_get_people(self):
        pwd = get_password({'system': 'ssh_system', 'username': 'teilnehmer'})
        self.assertIsNotNone(pwd)

if __name__ == '__main__':
    unittest.main()