class Person:
    def __init__ (self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

def main():
    p1 = Person("Sawitzki", "Rainer")
    print(p1.lastname)
    print(type(p1))
main()
