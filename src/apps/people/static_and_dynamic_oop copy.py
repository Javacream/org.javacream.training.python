class Person:
    # def __init__(to_initialize, lastname, firstname):
    #     to_initialize.lastname = lastname
    #     to_initialize.firstname = firstname
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    
    def info(self):
        return "a person: " + self.lastname + " " + self.firstname

sawitzki = Person("Sawitzki", "Rainer")
print(sawitzki.info())

sawitzki.height = 183
print(dir(sawitzki))
