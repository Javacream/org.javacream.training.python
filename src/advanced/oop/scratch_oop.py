class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        print(self.lastname)

class Student(Person):
    def __init__(self, lastname, firstname, university):
        #super().__init__(lastname, firstname)
        Person.__init__(self, lastname, firstname)
        #Other.__init__(self, lastname)
        #super(Other, self).__init__(lastname)
        self.university = university
    def study(self):
        print("studying")
    def say_hello(self):
        super().say_hello()
        print(f"the student {self.lastname}")

class Other:
    def __init__(self, name):
        self.name = name

p = Person("Sawitzki", "Rainer")
s = Student("Einstein", "Albert", "LMU")

# 
# p.say_hello()
s.say_hello()

# Person.say_hello(s)

#print(dir(s))