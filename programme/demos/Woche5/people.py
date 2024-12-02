class Person:
    def __init__(self, id, lastname, firstname, address):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.address = address

    def say_hello(self):
        message = f'Hello, my name is {self.firstname} {self.lastname}'
        return message

class Student(Person):
    def __init__(self, id, lastname, firstname, address, university):
        super().__init__(id, lastname, firstname, address)
        self.university = university
    def study(self):
        pass

class Address:
    def __init__(self, param_city, param_street):
        self.city = param_city
        self.street = param_street  
        self.people = set() 

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    person1 = Person(1, 'Musterperson', 'Andrea', a1)
    person2 = Person(2, 'Schneider', 'Hannah', a2)
    student1 = Student(3, 'Einstein', 'Albert', a1, 'LMU')
    print(person1.say_hello())
    print(student1.say_hello())
    print('done')

main()