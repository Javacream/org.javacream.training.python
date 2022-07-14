from enum import Enum
class Gender(Enum):
    MALE=1
    FEMALE=2
    DIVERSE=3

class Person:
    def __init__(self, lastname, firstname, height, gender):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender

    def say_hello(self):
        #so genannte String Interpolation
        return f"Hello, my name is {self.firstname} {self.lastname}"

#Besser, aber der Zugriff über den Index ist nicht sprechend 
person1 = Person("Sawitzki", "Rainer", 183, Gender.MALE)
person2 = Person("Meier", "Hannah", 199, Gender.DIVERSE)

print(person1.say_hello())