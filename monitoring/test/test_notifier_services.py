import unittest
import notifier_service
import monitoring_data as data
class ConsoleNotifierTest(unittest.TestCase):
    def test_send(self):
        console_notifier = notifier_service.ConsoleNotifier()
        console_notifier.send(data.Machine('TEST', '', None), [data.Metric('cpu', 95)])
        console_notifier.send(data.Machine('TEST', '', None), [data.Metric('memory', 95)])

if __name__ == '__main__':
    unittest.main()        