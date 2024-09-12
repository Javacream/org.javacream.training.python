from abc import ABC, abstractmethod
class Instrument(ABC):
    @abstractmethod
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
    pass

def application():
    #i = Instrument()
    g = Guitar()
    d = Drum()
    v = Violin()
    b = Bass()
    print(g.make_sound())
    print(d.make_sound())
    print(v.make_sound())
    print(b.make_sound())
application()