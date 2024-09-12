class FlyingMixin:
    def fly(self):
        return f"I am {self} and i can fly!"
class NameMixin:
    def __repr__(self):
        return f"a bird, name={self.name}"
    def __init__(self, name):
        self.name= name    

class Bird(FlyingMixin, NameMixin):
    def __init__(self, name):
        NameMixin.__init__(self, name)

class Plane(FlyingMixin):
    def __repr__(self):
        return "a plane"

def application():
    bird = Bird("blackbird")
    plane = Plane()
    print(bird.fly())
    print(plane.fly())

application()        