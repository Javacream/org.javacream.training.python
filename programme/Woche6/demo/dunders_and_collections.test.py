import unittest

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def __repr__(self):
        return f'Address: city={self.city}, street={self.street}'
    def __eq__(self, other):
        if isinstance(other, Address):
            return (self.city == other.city) and (self.street == other.street)
        else:
            return False
    def __hash__(self):
        return hash(self.city) + hash(self.street)
class AddressTests(unittest.TestCase):
    def test_address_equality(self):
        address_in_munich = Address("München", "Marienplatz")
        address_in_berlin = Address("Berlin", "Alexanderplatz")
        address_in_munich2 = Address("München", "Karlsplatz")
        address_in_munich3 = Address("München", "Karlsplatz")
        address_in_munich4 = address_in_munich3

        self.assertFalse(address_in_munich == address_in_berlin)
        self.assertFalse(address_in_munich == address_in_munich2)
        self.assertTrue(address_in_munich3 == address_in_munich2)
        self.assertTrue(address_in_munich3 == address_in_munich4)

        address_set = {address_in_munich, address_in_berlin, address_in_munich2, address_in_munich3, address_in_munich4}
        self.assertEqual(3, len(address_set))

if __name__ == '__main__':
    unittest.main()
