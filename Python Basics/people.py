class Person:
    def __init__(self, firstname, lastname, weight, height):
        self.firstname = firstname
        self.lastname = lastname
        self.weight = weight
        self.height = height
    def __repr__(self):
        return f'Person(firstname={self.firstname}, lastname={self.lastname}, weight={self.weight}, height={self.height})'
    def say_hello(self):
        return f'Hallo, mein Name ist {self.firstname} {self.lastname}'
    def get_bmi(self):
        return self.weight/(self.height ** 2)
