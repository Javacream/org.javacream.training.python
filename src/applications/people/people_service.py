class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'



