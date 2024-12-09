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
        return 'Zoing'
class Violin(Instrument):
    def make_sound(self):
        return 'FidelFadel'
class Drum(Instrument):
    def play(self):  # Die Methode soll doch "make_sound" heißen?
        return 'Wumm'
    def make_sound(self):
        return self.play()    

class Singer:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def sing(self):
        return "La la la"
class Orchester:
    def __init__(self):
        self.instruments = []
    def add(self, instrument: SoundProducer):
        if isinstance(instrument, SoundProducer):
            self.instruments.append(instrument)
        else:
            raise Exception(f'can only add SoundProducer, {instrument} is not')
    def concert(self):
        for instrument in self.instruments:
            print(instrument.make_sound())

def main():
    orchester = Orchester()
    # orchester.add(Instrument()) # WAS SOLL DAS?
    orchester.add(Violin())
    orchester.add(Guitar())
    orchester.add(Violin())
    orchester.add(Drum())
    orchester.add(Singer('Caruso', 'Eduardo'))
    orchester.concert()

if __name__ == '__main__':
    main()    