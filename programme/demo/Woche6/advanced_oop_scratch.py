class NameMixin:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'my name is {self.name}'

class FlyMixin:
    def fly(self):
        print(f'{self} and i can fly')

class Bird(FlyMixin, NameMixin):
    def __init__(self, name):
        NameMixin.__init__(self, name)


class Person(NameMixin):
    def __init__(self, name):
        NameMixin.__init__(self, name)

class Plane(FlyMixin):
    def __init__(self, type):
        self.type = type
    def __repr__(self):
        return f'a plane of type {self.type}'
    

def main():
    p = Person('Musterperson')
    b = Bird('Coco')
    p = Plane('Airbus')
    print(p, b)
    b.fly()
    p.fly()

if __name__ == '__main__':
    main()    