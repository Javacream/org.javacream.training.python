class Person:
    def __init__(self, lastname, firstname, weight, height):
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'