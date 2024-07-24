import time
class Machine:
    def __init__(self, name, ip, ressources) -> None:
        self.name = name
        self.ip = ip
        self.ressources = ressources
    def __repr__(self) -> str:
        return f'Machine: name={self.name}, ip={self.ip}, ressources={self.ressources}'
    def __eq__(self, other: object) -> bool:
        return self.name == other.name
    def __hash__(self) -> int:
        return hash(self.name)
class Ressource:
    def __init__(self, cpu, memory, storage) -> None:
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
    def __repr__(self) -> str:
        return f'CPU={self.cpu}, Memory={self.memory}, Storage={self.storage}'    

class Metric:
    def __init__(self, name, value) -> None:
        self.timestamp = time.time()
        self.value = value
        self.name = name
    def __repr__(self) -> str:
        return f"Metric: name={self.name}, value={self.value}, timestamp={self.timestamp}"

class Gauge(Metric):
    def __init__(self, name, value, min, max):
        super().__init__(name, value)
        self.min = min
        self.max = max
    def in_range(self):
        return self.min < self.value < self.max    

class Counter(Metric):
    def __init__(self, name, step, value=0):
        super().__init__(name, value)
        self.step = step

    def __repr__(self) -> str:
        return f"{super().__repr__()}, step={self.step}"
    def increment(self):
        self.value += self.step
    def reset(self):
        self.value = 0    


class Monitoring:
    def __init__(self):
        self.machines = dict()
        self.metrics = dict()
    def __collect_machines(self):
        with open ('./data/machines.csv') as machines_file:
            machines = dict()
            machine_data = machines_file.readlines()
            cleaned_machine_data = [element[:-1].split(',') for element in machine_data if len(element.strip()) > 1]
            for machine in cleaned_machine_data:
               name, ip, cpu, memory, storage = machine
               machines[name] = Machine(name, ip, Ressource(cpu, storage, memory))
            return machines
    def __collect_metrics(self):
        with open ('./data/metrics.csv') as metrics_file:
            metrics_data = metrics_file.readlines()
            cleaned_metrics_data = [element[:-1].split(',') for element in metrics_data if len(element.strip()) > 1]
            for metric_data in cleaned_metrics_data:
               machine_name, metric_name, metric_value = metric_data
               metric = Metric(metric_name, metric_value)
               machine = self.machines.get(machine_name)
               if machine is not None:
                metrics_list = self.metrics.get(machine)
                if metrics_list == None:
                    metrics_list = []
                    self.metrics[machine] = metrics_list
                metrics_list.append(metric)
    def collect(self):
        self.machines = self.__collect_machines()
        self.__collect_metrics()

    def get_metrics_for(self, machine_name):
        machine = self.machines.get(machine_name)
        return self.metrics.get(machine)

    def get_metrics(self, name):
        return [metric for metrics in self.metrics.values() for metric in metrics if metric.name == name]