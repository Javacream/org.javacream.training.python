import unittest
import collectors as c


class MetricsCollectorTest(unittest.TestCase):
    def setUp(self):
        self.machines_location = './data/machines.csv'
        self.metrics_location = './data/metrics.csv'
        
    def test_collect_metrics(self):
        machine_collector = c.MachinesCollector(self.machines_location)
        machines = machine_collector.collect_machines()
        metrics_collector = c.MetricsCollector(self.metrics_location)
        metrics = metrics_collector.collect_metrics(machines)
        self.assertEqual(3, len(metrics))
        self.assertTrue(2, len(metrics[machines.get('Database Server 1')]))

class MachineCollectorTest(unittest.TestCase):
        def setUp(self):
            self.machines_location = './data/machines.csv'

        def test_collect_machines(self):
            machine_collector = c.MachinesCollector(self.machines_location)
            machines = machine_collector.collect_machines()
            self.assertEqual(4, len(machines))
            self.assertTrue('Database Server 1' in machines)                

if __name__ == '__main__':
    unittest.main()