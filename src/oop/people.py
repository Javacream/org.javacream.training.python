class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def __repr__(self):
        return f'Address(city={self.city}, street={self.street})'

class Person:
    def __init__(self, lastname, firstname, address, height=170, weight=67):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height / 100
        self.weight = weight
        self.addresses = {address}
        self.name = f'{self.firstname} {self.lastname}'
    def say_hello(self):
        return f'Hello, my name is {self.name}, i live in {self.addresses}'
    def get_bmi(self):
        height = self.height
        return self.weight/(height**2)

class Student(Person):
    def __init__(self, lastname, firstname, address, university, height=170, weight=67):
        super().__init__(lastname, firstname, address, height, weight)
        self.university = university

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    person1 = Person('Sawitzki', 'Rainer', a1, 183, 75.8)
    person2 = Person('Muster', 'Hannah', a2, 783, 55.8)
    person1.addresses.add(a2)
    student1 = Student('Einstein', 'Albert', a1, 'LMU')

    print(person1.say_hello())
    print(person2.say_hello())
    print(person1.get_bmi())
    print(student1.get_bmi())
    print(person1)
    print('done')

main()
