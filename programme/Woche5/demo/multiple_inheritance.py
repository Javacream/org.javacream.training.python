class House:
    def __init__(self, rooms, floors):
        self.rooms = rooms
        self.floors = floors

class Boat:
    def __init__(self, max_speed, depth):
        self.max_speed = max_speed
        self.depth = depth
    def drive(self):
        print(f'moving on with max speed {self.max_speed}')
class HouseBoat(House, Boat): # Das erste Element in der Aufzählung ist eine richtige Superklasse
    def __init__(self, rooms, floors, max_speed, depth):
        super().__init__(rooms, floors) # Hier: Klasse House
        #House.__init__(self) # Hier: Klasse House
        Boat.__init__(self, max_speed, depth)

def main():
    house_boat = HouseBoat(12, 2, 42, 10)
    house_boat.drive()
    print(house_boat)

if __name__ == '__main__':
    main()