from abc import ABC, abstractmethod
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

class Singer(Instrument): # a singer is an instrument???
    def make_sound(self):
        return "La la la"

class Orchester:
    def __init__(self):
        self.instruments = []
    def concert(self):
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
