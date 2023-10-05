

class Person:
    # a static attribute, part of the class object
    info_template = "Hello, my name is {} {}"

    # constructor
    def __init__(self, lastname, firstname, height):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height

    def info(self):
        return Person.info_template.format(self.firstname, self.lastname)

def main():
    p1 = Person("Goo", "Georg", "big")
    p2 = Person("Foo", "Henry", "small")
    print(p1.info())
    print(p2.info())

main()