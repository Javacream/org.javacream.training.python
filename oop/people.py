class Person:
    allowedGenders = ('m', 'f', 'd')
    def __init__(self, lastname, firstname, height, gender):
        heightAsNumber = int(height)
        if heightAsNumber <=25:
            raise Exception(f"invalid height, must be greater than 25, was {heightAsNumber}")
        if not gender in Person.allowedGenders:
            raise Exception(f"invalid gender, must be (m, f, d)), was {gender}")
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender
    def sayHello(self):
        helloMessage = f"Hello, my name is {self.firstname} {self.lastname}"
        return helloMessage
    def marry(self, newPartner):
        self.partner = newPartner
        newPartner.partner = self
    def divorce(self):
        self.partner.partner= None    
        self.partner = None
    
def test():
    p1 = Person("Sawitzki", "Rainer", 183, 'm')
    p2 = Person("Meier", "Hannah", 199, 'd')
    p3 = Person("Schneider", "Andrea", 155, 'f')

    p1.marry(p2)
    p2.divorce()
    p1.marry(p3)

    print("marriage done")

test()