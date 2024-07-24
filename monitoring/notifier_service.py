def notify_console(machine, alarms):
    for alarm in alarms:
        print(f'for machine {machine.name} a {alarm.name} limit was detected: {alarm.value}')
