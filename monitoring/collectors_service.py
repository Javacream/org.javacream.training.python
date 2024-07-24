import monitoring_data as data
class MachinesCollector:
    def __init__(self, location) -> None:
        self.location = location
    def collect_machines(self):
        with open (self.location) as machines_file:
            machines = dict()
            machine_data = machines_file.readlines()
            cleaned_machine_data = [element[:-1].split(',') for element in machine_data if len(element.strip()) > 1]
            for machine in cleaned_machine_data:
               name, ip, cpu, memory, storage = machine
               machines[name] = data.Machine(name, ip, data.Ressource(cpu, storage, memory))
            return machines

class MetricsCollector:
    def __init__(self, location) -> None:
        self.location = location
    def collect_metrics(self):
        with open (self.location) as metrics_file:
            machines = self.machines_collector.collect_machines()
            metrics = dict()
            metrics_data = metrics_file.readlines()
            cleaned_metrics_data = [element[:-1].split(',') for element in metrics_data if len(element.strip()) > 1]
            for metric_data in cleaned_metrics_data:
               machine_name, metric_name, metric_value = metric_data
               metric = data.Metric(metric_name, int(metric_value))
               machine = machines.get(machine_name)
               if machine is not None:
                metrics_list = metrics.get(machine)
                if metrics_list == None:
                    metrics_list = []
                    metrics[machine] = metrics_list
                metrics_list.append(metric)
            return metrics
