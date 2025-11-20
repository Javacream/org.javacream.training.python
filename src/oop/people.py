class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Person:
    def __init__(self, lastname, firstname, address, height=170, weight=67):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height / 100
        self.weight = weight
        self.address = address
        self.name = f'{self.firstname} {self.lastname}'
    def say_hello(self):
        return f'Hello, my name is {self.name}, i live in {self.address.city}'
    def get_bmi(self):
        height = self.height
        return self.weight/(height**2)


def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    person1 = Person('Sawitzki', 'Rainer', a1, 183, 75.8)
    person2 = Person('Muster', 'Hannah', a2, 783, 55.8)
    person3 = Person('Musterperson', 'Andrea', a1)
    person1_dict = {'lastname': 'A', 'firstname': 'B', 'height': 183, 'weight': 75.9}
    person2_dict = {'last': 'A', 'first': 'B', 'h': 183, 'w': 75.9, 'eye_color': 'blue'}


    print(person1.say_hello())
    print(person2.say_hello())
    print(person1.get_bmi())
    print('done')

main()
