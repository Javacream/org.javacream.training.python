class Person:
    def __init__ (self, lastname, firstname=""):
        if lastname == None:
            raise Exception("lastname is mandatory")
        self.lastname = lastname
        self.firstname = firstname
    def __greet(self):
        return f'Hello, i am {self.firstname} {self.lastname}'
    def greet(self):
        return f'Hello, i am {self.firstname} {self.lastname}'


def main():
    p1 = Person("Sawitzki", "Rainer")
    p2 = Person("Meier", "Andrea")
    # p3 = Person(None, None)
    p3 = Person("Sawitzki")
    print(p1.greet())
    print(p3.greet())
    p1.weight = 75
    print(p1.weight)    
main()
