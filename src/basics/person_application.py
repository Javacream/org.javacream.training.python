class Person:
    def __init__(self, lastname, firstname, height, gender):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender

    def say_hello(self):
        return "Hello, my name is " + self.firstname + " " + self.lastname
 
person1 = Person("Sawitzki", "Rainer", 183, 'm')
person2 = Person("Meier", "Hannah", 199, 'd')

print(person1.say_hello())