class FlyingMixin:
    def fly(self):
        return f"I am {self} and i can fly!"
class NameMixin:
    def __repr__(self):
        return f"Name: {self.name}"
    def __init__(self, name):
        self.name= name    

class Bird(FlyingMixin, NameMixin):
    def __init__(self, name):
        NameMixin.__init__(self, name)

class Plane(FlyingMixin):
    pass

def test():
    bird = Bird("blackbird")
    plane = Plane()
    print(bird)
    print(bird.fly())
    print(plane)
    print(plane.fly())

test()        