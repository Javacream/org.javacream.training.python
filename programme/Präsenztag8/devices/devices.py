class Device:
    def __init__(self, id: int, name: str, ports:list[int], status:bool):
        self.id = id
        self.name = name
        self.ports = ports
        self.status = status
    def __repr__(self):
        return f'Device(id={self.id}, name={self.name}, ports={self.ports}, status={self.status})'
    def __eg__(self, other_device):
        if isinstance(other_device, Device):
            return self.id == other_device.id
        else:
            return False
    def __hash__(self):
        return hash(self.id)