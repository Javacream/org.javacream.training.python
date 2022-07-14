class Person:
    Gender = ('m', 'f', 'd')
    def __init__(self, lastname, firstname, height, gender):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender

    def say_hello(self):
        #so genannte String Interpolation
        return f"Hello, my name is {self.firstname} {self.lastname}"

#Besser, aber der Zugriff über den Index ist nicht sprechend 
person1 = Person("Sawitzki", "Rainer", 183, Person.Gender[0])
person2 = Person("Meier", "Hannah", 199, Person.Gender[2])

print(person1.say_hello())