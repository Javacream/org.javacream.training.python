from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
class Instrument(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class SoundProducer(Protocol):
    def make_sound(self):
        pass

class Guitar(Instrument):
    def make_sound(self):
        return 'Klimper'
class Drum(Instrument):
    def make_sound(self):
        return 'Wumm'
class Violin(Instrument):
    def play(self):
        return "Fidel"
    def make_sound(self):
        return self.play()

class Bass(Instrument):
    def make_sound(self):
        return 'wummer'

class Singer:
    def sing(self):
        return "La lala"
    def make_sound(self):
        return self.sing()
    

class Orchester:
    def __init__(self) -> None:
        self.members = []
    def concert(self):
        member: SoundProducer
        for member in self.members:
            print(member.make_sound())    

def application():
    o = Orchester()
    o.members.append(Guitar())
    o.members.append(Drum())
    o.members.append(Violin())
    o.members.append(Bass())
    o.members.append(Singer())

    o.concert()
application()