class FlyMixin:
    def fly(self):
        return f'i am {self} and i can fly'

class NameMixin:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Nameable, name = {self.name}' 

class Plane(FlyMixin):
    pass       

class Bird(FlyMixin, NameMixin):
    def __init__(self, name):
        NameMixin.__init__(self, name)       

def main():
    #f = FlyMixin()
    #print(f.fly())
    #n = NameMixin('Hugo')
    #print(n)
    
    p = Plane()
    print(p.fly())
    b = Bird('Rudi')
    print(b.fly())

if __name__ == '__main__':
    main()    