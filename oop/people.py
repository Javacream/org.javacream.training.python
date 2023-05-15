class Person:
    allowedGenders = ('m', 'f', 'd')
    def __init__(self, lastname, firstname, height, gender):
        heightAsNumber = int(height)
        if heightAsNumber <=25:
            raise Exception(f"invalid height, must be greater than 25, was {heightAsNumber}")
        if not gender in self.allowedGenders:
            raise Exception(f"invalid gender, must be (m, f, d)), was {gender}")
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender
    def sayHello(self):
        helloMessage = f"Hello, my name is {self.firstname} {self.lastname}"
        return helloMessage
    
def test():
    p1 = Person("Sawitzki", "Rainer", 183, 'm')
    print(p1.sayHello())
    try:
        p = Person("Sawitzki", "Rainer", 1, 'm')
        print("WARNING: AN EXCEPTION MUST BE THROWN BECAUSE HEIGHT IS INVALID!")
    except:
        pass    
    try:
        p = Person("Sawitzki", "Rainer", 183, 'b')
        print("WARNING: AN EXCEPTION MUST BE THROWN BECAUSE GENDER IS INVALID!")
    except:
        pass    


test()