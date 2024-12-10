import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self) -> float:
        pass
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    def perimeter(self) -> float:
        return 2 * self.radius * math.pi
    def area(self) -> float:
        return self.radius * self.radius * math.pi

class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    def perimeter(self) -> float:
        return 2 * (self.height + self.width)
    def area(self) -> float:
        return self.height * self.width
    
def application():
    c = Circle(3)
    print(c.perimeter())
    r = Rectangle(3, 4)
    print(r.perimeter())

application()    