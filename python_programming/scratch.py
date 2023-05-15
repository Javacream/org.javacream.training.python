class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def sayHello(self):
        return f"Hello, my name is {self.firstname} {self.lastname}"

def main():
    personMeier = Person("Meier", "Hannah")
    personMeier.middleName = "Hugo"
    personSawitzki = Person("Sawitzki", "Rainer")
    print(personSawitzki.sayHello())
    print(personMeier.sayHello())
main()