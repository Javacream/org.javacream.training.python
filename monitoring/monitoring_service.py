import collectors
class Monitoring:
    def __init__(self, machines_location, metrics_location):
        self.machines = dict()
        self.metrics = dict()
        self.machines_collector = collectors.MachinesCollector(machines_location)
        self.metrics_collector = collectors.MetricsCollector(metrics_location)

    def collect(self):
        self.machines = self.machines_collector.collect_machines()
        self.metrics = self.metrics_collector.collect_metrics(self.machines)

    def get_metrics_for(self, machine_name):
        machine = self.machines.get(machine_name)
        return self.metrics.get(machine)

    def get_metrics(self, name):
        return [metric for metrics in self.metrics.values() for metric in metrics if metric.name == name]
    

