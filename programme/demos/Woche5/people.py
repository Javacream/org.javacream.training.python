class Person:
    def __init__(self, id, lastname, firstname, *addresses):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.addresses = set(addresses)
        for address in addresses:
            address.people.add(self)
            
    def say_hello(self):
        message = f'Hello, my name is {self.firstname} {self.lastname}'
        return message


class Address:
    def __init__(self, param_city, param_street):
        self.city = param_city
        self.street = param_street  
        self.people = set() 

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    person1 = Person(1, 'Musterperson', 'Andrea', a1, a2)
    person2 = Person(2, 'Schneider', 'Hannah', a2)
    #person1.addresses.add(a2)
    print(person1.say_hello())
    print(person2.say_hello())
    print('done')

main()