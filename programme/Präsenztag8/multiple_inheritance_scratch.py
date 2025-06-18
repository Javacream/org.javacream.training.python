class House:
    def __init__(self, rooms):
        self.rooms = rooms
        print(f'erzeuge Haus')
class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        print(f'erzeuge Boot')

class HouseBoat(House,  Boat):
    def __init__(self, rooms, max_speed):
        House.__init__(self, rooms)
        Boat.__init__(self, max_speed)
        print(f'erzeuge Hausboot')


def main():
    h = House(4)
    b = Boat(1.55)
    hb = HouseBoat(2, 0.77)
    print(isinstance(h, House))
    print(isinstance(b, House))
    print(isinstance(hb, HouseBoat))
    print(isinstance(hb, House))
    print(isinstance(hb, Boat))

if __name__ == '__main__':
    main()