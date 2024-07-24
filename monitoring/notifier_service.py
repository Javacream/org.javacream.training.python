class ConsoleNotifier:
    def send(self, machine, alarms):
        for alarm in alarms:
            print(f'for machine {machine.name} a {alarm.name} limit was detected: {alarm.value}')
