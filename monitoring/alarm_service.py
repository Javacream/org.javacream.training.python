class AlarmManager:
    def __init__(self, cpu_limit, memory_threshold):
        self.cpu_limit = cpu_limit
        self.memory_threshold = memory_threshold

    def check(self):
            self.monitoring.collect()
            machines = self.machines_collector.collect_machines()
            for machine in machines:
                self.__check_machine(machine)

    def __check_machine(self, machine):
         
         metrics = self.monitoring.get_metrics_for(machine)
         cpu_alarms = [metric for metric in metrics if  metric.name == 'cpu' and metric.value >= self.cpu_limit]
         self.notifier.send(machine, cpu_alarms)
         memory_alarms = [metric for metric in metrics if  metric.name == 'memory' and metric.value >= self.memory_threshold/100 * machine.ressource.memory]
         self.notifier.send(machine, memory_alarms)
