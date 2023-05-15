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
        if hasattr(self, "partner") and self.partner:
            raise Exception("cannot marry because i am already married")
        if hasattr(newPartner, "partner") and newPartner.partner:
            raise Exception("cannot marry because newPartner am already married")
        if not newPartner:
            raise Exception("cannot marry non existing newPartner")
        if newPartner == self:
            raise Exception("cannot marry myself")
        self.partner = newPartner
        newPartner.partner = self
    def divorce(self):
        if not hasattr(self, "partner") or not self.partner:
            raise Exception("cannot divorce, i am not married")
        self.partner.partner= None    
        self.partner = None
    
def test():
    p1 = Person("Sawitzki", "Rainer", 183, 'm')
    p2 = Person("Meier", "Hannah", 199, 'd')
    p3 = Person("Schneider", "Andrea", 155, 'f')
    try:
        p1.marry(None)
        print("EXCEPTION MUST BE THROWN, marry with None not allowed")
    except:
        pass    
    try:
        p1.marry(p1)
        print("EXCEPTION MUST BE THROWN, marry yourself not allowed")
    except:
        pass    
    try:
        p1.divorce()
        print("EXCEPTION MUST BE THROWN, p1 is not married")
    except:
        pass    

    p1.marry(p2)
    try:
        p3.marry(p2)
        print("EXCEPTION MUST BE THROWN, p2 ist married!")
    except:
        pass    
    p2.divorce()
    p3.marry(p2)
    try:
        p1.divorce()
        print("EXCEPTION MUST BE THROWN, p1 is not married")
    except:
        pass    

    print("marriage done")

test()