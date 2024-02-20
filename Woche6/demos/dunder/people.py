class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def introduce(self):
        return f"I am {self.firstname} {self.lastname}"
    def __repr__(self):
        return f"Person: lastname={self.lastname}, firstname={self.firstname}"

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

def test():
    sawitzki = Person("Sawitzki", "Rainer")
    einstein = Student("Einstein", "Albert", "LMU München")
    print(sawitzki)
    print(einstein)
    print(str(sawitzki))
test()    