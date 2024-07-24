import unittest
import context
import monitoring_data as data
class AlarmManagerTest(unittest.TestCase):
    def test_check_alarms(self):
        alarm_manager = context.alarm_manager
        alarm_manager.check()

if __name__ == '__main__':
    unittest.main()    