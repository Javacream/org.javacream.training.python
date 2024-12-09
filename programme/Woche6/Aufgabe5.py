from typing import Protocol, runtime_checkable

@runtime_checkable
class Runner(Protocol):
    def start(self):
        pass
    def stop(self):
        pass


class Vehicle:
    def start(self):
        print("vehicle is starting")
    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle):
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stopping")

class Motorbike(Vehicle):
    def start(self):
        print("motorbike is starting")
    def stop(self):
        print("motorbike is stopping")

def main():
    m = Motorbike()
    print(isinstance(m, Runner))

if __name__ == '__main__':
    main()