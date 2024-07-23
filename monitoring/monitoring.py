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
        return self.name.__hash__()
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
        self.data = dict()
    def collect(self):
        with open ('./data/machines.csv') as machines_file:
            data = machines_file.readlines()
            data = [element[:-1].split(',') for element in data]
            for machine in data:
               self.data[machine[0]] = (Machine(machine[0], machine[1], Ressource(machine[2], machine[3], machine[4])), [])
        with open ('./data/metrics.csv') as metrics_file:
            data = metrics_file.readlines()
            data = [element[:-1].split(',') for element in data]
            # print(data)
            for metric in data:
               self.data[metric[0]][1].append(Metric(metric[1], metric[2]))

    def get_metrics_for(self, machine_name):
        return self.data.get(machine_name)
    def get_metrics(self, name):
        return [metric for data in self.data.values() for metric in data[1] if metric.name == name]