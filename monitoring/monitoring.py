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

def test():
    machine1 = Machine("Database Server 1", "1.2.3.4", Ressource(8, '128G', '4TB'))
    machine2 = Machine("Web Server 1", "1.2.3.5", Ressource(8, '128G', '4TB'))
    metric1 = Gauge('CPU Utilization Percent', 78, 0, 100)
    metric2 = Counter('Http Request', 5)
    metric3 = Gauge('Storage GB', 123.45, 2,4)
    machine_x = Machine("Database Server 1", "1.2.3.6", Ressource(8, '256G', '4TB'))

    print(machine1)
    print(machine1 == machine_x)
    print(metric2)
    print(metric1.in_range())
test()
