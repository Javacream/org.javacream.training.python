import unittest
import monitoring as m
class MonitoringTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self) -> None:
        pass

    def test_machines_are_equal_by_name(self):
        machine1 = m.Machine("Database Server 1", "1.2.3.4", m.Ressource(8, '128G', '4TB'))
        machine2 = m.Machine("Database Server 1", "1.2.3.5", m.Ressource(8, '128G', '4TB'))
        self.assertEqual(machine1, machine2)

    def test_machines_are_not_equal_by_different_name(self):
        machine1 = m.Machine("Database Server 1", "1.2.3.4", m.Ressource(8, '128G', '4TB'))
        machine2 = m.Machine("Web Server 1", "1.2.3.5", m.Ressource(8, '128G', '4TB'))
        self.assertNotEqual(machine1, machine2)

if __name__ == '__main__':
    unittest.main()