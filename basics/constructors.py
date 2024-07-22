class Person:
    def __init__ (self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def greet(self):
        return f'Hello, i am {self.firstname} {self.lastname}'

def main():
    p1 = Person("Sawitzki", "Rainer")
    p2 = Person("Meier", "Andrea")
    print(p1.greet())
    print(p2.greet())
main()
