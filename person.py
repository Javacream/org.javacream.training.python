class Person:
    def __init__(self, lastname, firstname, height, weight): # Constructor
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight


p1 = Person("Sawitzki", "Rainer", 183, 81)
print(p1.lastname)
p2 = Person("Mustermann", "Andrea", 176, 66)
print(p2.lastname)



