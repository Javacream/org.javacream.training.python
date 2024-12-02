class Person:
    def __init__(self, id, lastname, firstname):  # Der Konstruktor der Klasse Person
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        message = f'Hello, my name is {self.firstname} {self.lastname}'
        return message


class Address:
    def __init__(self, param_city, param_street):
        self.city = param_city
        self.street = param_street   

person1 = Person(1, 'Musterperson', 'Andrea')
person2 = Person(2, 'Schneider', 'Hannah')

print(person1.say_hello())
print(person2.say_hello())
print('done')
