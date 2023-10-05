class Person:
    # constructor
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def info(self):
        return "Hello, my name is " + self.lastname

def main():
    p1 = Person("Goo", "Georg")
    p2 = Person("Foo", "Henry")
    print(type(p1), type(p2))
    #print(p1.name, p2.name)
    print(p1.info(), p2.info())
main()