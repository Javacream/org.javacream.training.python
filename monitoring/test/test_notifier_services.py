import unittest
import notifier_service
import monitoring_data as data
class ConsoleNotifierTest(unittest.TestCase):
    def test_send(self):
        notify = notifier_service.notify_console
        notify(data.Machine('TEST', '', None), [data.Metric('cpu', 95)])
        notify(data.Machine('TEST', '', None), [data.Metric('memory', 95)])

if __name__ == '__main__':
    unittest.main()        