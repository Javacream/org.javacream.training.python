class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
    

class Student(Person):
    def __init__(self, lastname, firstname, university):
        super().__init__(lastname, firstname)
        self.university = university
    def study(self):
        return f'{self.say_hello()}, studying at {self.university}'

class Worker(Person):
    def __init__(self, lastname, firstname, company):
        super().__init__(lastname, firstname)
        self.company = company
    def study(self):
        return f'{self.say_hello()}, working at {self.company}'

