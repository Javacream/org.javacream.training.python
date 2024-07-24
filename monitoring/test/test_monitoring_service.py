import unittest
import monitoring_service as service
import monitoring_data as data
class MonitoringTests(unittest.TestCase):
    def setUp(self):
        self.machines_location = './data/machines.csv'
        self.metrics_location = './data/metrics.csv'

    def tearDown(self) -> None:
        pass

    def test_machines_are_equal_by_name(self):
        machine1 = data.Machine("Database Server 1", "1.2.3.4", data.Ressource(8, '128G', '4TB'))
        machine2 = data.Machine("Database Server 1", "1.2.3.5", data.Ressource(8, '128G', '4TB'))
        self.assertEqual(machine1, machine2)

    def test_machines_are_not_equal_by_different_name(self):
        machine1 = data.Machine("Database Server 1", "1.2.3.4", data.Ressource(8, '128G', '4TB'))
        machine2 = data.Machine("Web Server 1", "1.2.3.5", data.Ressource(8, '128G', '4TB'))
        self.assertNotEqual(machine1, machine2)

    def test_collected_metrics_are_available(self):
        monitoring = service.Monitoring(self.machines_location, self.metrics_location)
        monitoring.collect()
        self.assertEqual(2, len(monitoring.get_metrics_for('Database Server 1')))
    
    def test_cpu_metrics_are_availabe(self):
        monitoring = service.Monitoring(self.machines_location, self.metrics_location)
        monitoring.collect()
        self.assertEqual(1, len(monitoring.get_metrics('cpu')))

if __name__ == '__main__':
    unittest.main()