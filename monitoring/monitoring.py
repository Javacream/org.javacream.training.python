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
    initial = 0 # Das ist ein static Attribute
    @staticmethod # Dekoration, Annotation, die dem Interpreter zeigt, dass die Methode staisch sein soll
    def static_method_demo():
        print("*****************")
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
    metric4 = Counter('Http Request', 123)
    machine_x = Machine("Database Server 1", "1.2.3.6", Ressource(8, '256G', '4TB'))

    print(metric2.initial)    
    print(metric4.initial)    
    Counter.initial = -5
    print(metric2.initial)    
    print(metric4.initial) 

    metric2.initial = 42 # VORSICHT: Hier bekommt das von metric2 referenzierte Objekt eine neu Eigenschaft initial
    print(metric2.initial)    
    print(metric4.initial) 
    Counter.static_method_demo()

test()
