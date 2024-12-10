class Instrument:
    def __init__(self, category):
        self.category = category
    def play():
        pass

class Orchester:
    def __init__(self):
        self.instruments = []
    def concert(self):
        for instrument in self.instruments:
            print(instrument.play())
class Guitar(Instrument):
    def __init__(self):
        super().__init__('string')
    def play(self):
        return 'Klimper'    
class Violin(Instrument):
    def __init__(self):
        super().__init__('string')
    def play(self):
        return 'Fidel'    

def main():
    orchester = Orchester()
    orchester.instruments.append(Guitar())
    orchester.instruments.append(Violin())
    orchester.instruments.append(Guitar())
    orchester.concert()

if __name__ == '__main__':
    main()    