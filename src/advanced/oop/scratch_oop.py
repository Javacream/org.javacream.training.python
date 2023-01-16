#class Person:
    #lastname, firstname


#class Person(lastname, firstname)

class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

p = Person("Sawitzki", "Rainer")

X = Person

p2 = X("A", "B")
print(p2.lastname)

class Object:
    pass

o = Object()
Person.__init__(o, "47", "11")
print(o.lastname)

    