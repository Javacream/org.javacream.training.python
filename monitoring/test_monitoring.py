import unittest
import monitoring as m
class MonitoringTests(unittest.TestCase):
    def setUp(self):
        self.location = './data/machines.csv'

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

    def test_collected_metrics_are_available(self):
        monitoring = m.Monitoring(self.location)
        monitoring.collect()
        self.assertEqual(2, len(monitoring.get_metrics_for('Database Server 1')))
    
    def test_cpu_metrics_are_availabe(self):
        monitoring = m.Monitoring(self.location)
        monitoring.collect()
        self.assertEqual(1, len(monitoring.get_metrics('cpu')))

    def test_collect_metrics(self):
        monitoring = m.Monitoring(self.location)
        machine_collector = m.MachinesCollector(self.location)
        machines =machine_collector.collect_machines()
        metrics = monitoring._Monitoring__collect_metrics(machines)
        self.assertEqual(3, len(metrics))
        self.assertTrue(2, len(metrics[machines.get('Database Server 1')]))
        

class MachineCollectorTest(unittest.TestCase):
        def test_collect_machines(self):
            location = './data/machines.csv'
            machine_collector = m.MachinesCollector(location)
            machines = machine_collector.collect_machines()
            self.assertEqual(4, len(machines))
            self.assertTrue('Database Server 1' in machines)                

if __name__ == '__main__':
    unittest.main()