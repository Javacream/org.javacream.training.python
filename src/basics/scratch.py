#person_lastname = "Sawitzki"
#person_firstname = "Rainer"
class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

person1 = Person("Sawitzki", "Rainer")
person2 = Person("Meier", "Hannah")

print("finished")