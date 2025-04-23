from abc import ABC, abstractmethod

class MusicInstrument(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(MusicInstrument):
    def play(self):
        return "Klimper klamper"
        
class Violin(MusicInstrument):
    def play(self):
        return "Fidel fadel"

class Drum(MusicInstrument):
    def play(self):
        return "Wumm"    
