from abc import ABC, abstractmethod

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
class Orchester:
    def __init__(self):
        self.instruments = []
    def add(self, instrument: Instrument):
        self.instruments.append(instrument)
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
    orchester.concert()

if __name__ == '__main__':
    main()    