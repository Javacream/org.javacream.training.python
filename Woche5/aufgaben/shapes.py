import math
class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * math.pi
    def perimeter(self):
        return 2*self.radius*math.py
