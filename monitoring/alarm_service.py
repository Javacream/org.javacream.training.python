class AlarmManager:
    def __init__(self, cpu_limit, memory_threshold):
        self.cpu_limit = cpu_limit
        self.memory_threshold = memory_threshold

    def check(self):
            self.monitoring.collect()
            machines = list(self.machines_collector.collect_machines().values())
            for machine in machines:
              self.__check_machine(machine)

    def __check_machine(self, machine):
         metrics = self.monitoring.get_metrics_for(machine.name)
         cpu_alarms = [metric for metric in metrics if  metric.name == 'cpu' and metric.value >= self.cpu_limit]
         self.notify(machine, cpu_alarms)
         memory_alarms = [metric for metric in metrics if  metric.name == 'ram' and metric.value >= self.memory_threshold/100 * machine.resources.memory]
         self.notify(machine, memory_alarms)
