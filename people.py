class Person:
    # constructor
    def __init__(self, lastname, firstname, height):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height

    def info(self):
        info_template = "Hello, my name is {} {}"
        return info_template.format(self.firstname, self.lastname)

def main():
    p1 = Person("Goo", "Georg", 188)
    p2 = Person("Foo", "Henry", 166)
    print(p1.info())
    print(p2.info())

main()