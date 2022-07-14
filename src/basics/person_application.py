class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def say_hello(self):
        return "hello, my name is " + self.lastname

person1 = Person("Sawitzki", "Rainer")
person2 = Person("Meier", "Hannah")

print(person1.say_hello())