from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

@runtime_checkable
class SoundProducer(Protocol):
    def make_sound(self):
        pass
    
class Instrument(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Guitar(Instrument):
    def make_sound(self):
        return "Klimper"
    
class Drum(Instrument):
    def make_sound(self):
        return "Wumm"

class Violin(Instrument):
    def play(self):
        return "Fiedel"
    def make_sound(self):
        return self.play()

class Singer:
    def sing(self):
        return "La la la"
    def make_sound(self):
        return self.sing()
    

class Orchester:
    def __init__(self):
        self.instruments = []
    def concert(self):
        instrument: SoundProducer
        for instrument in self.instruments:
            print(instrument.make_sound())

def test():
    orchester = Orchester()
    orchester.instruments.append(Guitar())
    orchester.instruments.append(Drum())
    orchester.instruments.append(Violin())
    orchester.instruments.append(Singer())
    orchester.concert()
test()
