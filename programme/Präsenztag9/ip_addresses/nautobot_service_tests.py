import unittest
from nautobot_service import NautobotService

class NautobotServiceTests(unittest.TestCase):
    def test_ip_address_has_expected_format(self):
        NAUTOBOT_URL = 'https://demo.nautobot.com/api/'
        API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        nautobot_service = NautobotService(NAUTOBOT_URL, API_TOKEN)
        ip_addresses = nautobot_service.get_ip_addresses()
        expected_keys = ['id', 'object_type', 'display', 'url', 'natural_slug', 'address', 
'host', 'mask_length', 'type', 'ip_version', 'dns_name', 'description', 'status', 'role', 'parent', 'tenant', 'nat_inside', 'created', 'last_updated', 'tags', 'notes_url', 'custom_fields', 'nat_outside_list', 'interfaces', 'vm_interfaces']
        for key in expected_keys:
            for ip_address in ip_addresses:
                self.assertIn(key, ip_address.keys())
    def test_has_50_ap_addresses(self):
        expected_length = 50
        NAUTOBOT_URL = 'https://demo.nautobot.com/api/'
        API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        nautobot_service = NautobotService(NAUTOBOT_URL, API_TOKEN)
        ip_addresses = nautobot_service.get_ip_addresses()
        self.assertEqual(expected_length, len(ip_addresses))
if __name__ == '__main__':
    unittest.main()