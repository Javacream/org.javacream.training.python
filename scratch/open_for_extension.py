class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def sayHello(self):
        format = 'my name is {} {}'
        return format.format(self.firstname, self.lastname)

class PersonSlot:
    __slots__ = ["lastname", "firstname"]
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def sayHello(self):
        format = 'my name is {} {}'
        return format.format(self.firstname, self.lastname)


def person_demo():
    p = Person("Sawitzki", "Rainer")
    p2 = Person("Mustermann", "Hanna")
    p2.height=183
    print(p.sayHello())
    del p.lastname
    print(dir(p))
    print(dir(p2))

def person_slot_demo():
    p = PersonSlot("Sawitzki", "Rainer")
    p2 = PersonSlot("Mustermann", "Hanna")
    #p2.height=183
    del p.lastname
    print(p.sayHello())
    print(dir(p))
    print(dir(p2))

if __name__ == '__main__':
    person_slot_demo()