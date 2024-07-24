import unittest
import context

class MetricsCollectorTest(unittest.TestCase):
    def test_collect_metrics(self):
        machine_collector = context.machines_collector
        machines = machine_collector.collect_machines()
        metrics_collector = context.metrics_collector
        metrics = metrics_collector.collect_metrics(machines)
        self.assertEqual(3, len(metrics))
        self.assertTrue(2, len(metrics[machines.get('Database Server 1')]))

class MachineCollectorTest(unittest.TestCase):
        def test_collect_machines(self):
            machines_collector = context.machines_collector
            machines = machines_collector.collect_machines()
            self.assertEqual(4, len(machines))
            self.assertTrue('Database Server 1' in machines)                

if __name__ == '__main__':
    unittest.main()