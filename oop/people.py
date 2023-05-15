class Person:
    def __init__(self, lastname, firstname, height, gender):
        heightAsNumber = int(height)
        if heightAsNumber <=25:
            raise Exception(f"invalid height, must be greater than 25, was {heightAsNumber}")
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
        print("WARNING: AN EXCEPTION MUST BE THROWN!")
    except:
        pass    


test()