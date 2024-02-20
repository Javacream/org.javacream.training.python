class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def introduce(self):
        return f"I am {self.firstname} {self.lastname}"
    
class Student(Person):
    def __init__(self, lastname, firstname, university):
        super().__init__(lastname, firstname)
        self.university = university
    def study(self):
        return f"doing some studies at {self.university}"
    def introduce(self):
        introduction = super().introduce()
        introduction += f", studying at {self.university}"
        return introduction

class Worker(Person):
    def __init__(self, lastname, firstname, company, salary):
        super().__init__(lastname, firstname)
        self.company = company
        self.salary = salary
    def work(self):
        return f"doing work at {self.company}"
    def introduce(self):
        #introduction = super().introduce()
        introduction = f"Working at {self.company}"
        return introduction


def test():
    sawitzki = Person("Sawitzki", "Rainer")
    einstein = Student("Einstein", "Albert", "LMU München")
    schufter = Worker("Schufter", "Andrea", "Cegos", 42)
    print(sawitzki.introduce())
    print(einstein.introduce())
    print(schufter.introduce())
    print(einstein.study())
    print(schufter.work())


test()    