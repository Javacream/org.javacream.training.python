class Person:
    def __init__(self, lastname, firstname, address):
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
    def say_hello(self):
        greeting = f'Hallo, mein Name ist {self.firstname} {self.lastname}'
        return greeting

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student(Person):
    def __init__(self, lastname, firstname, address, university):
        self.university = university
        super().__init__(lastname, firstname, address)
    def study(self):
        print(f'ich studiere an {self.university}')    
class Worker(Person):
    def __init__(self, lastname, firstname, address, company):
        super().__init__(lastname, firstname, address)
        self.company = company
    def work(self):
        print(f'ich arbeite bei {self.company}')    

def main():
    address_in_munich = Address("München", "Marienplatz")
    address_in_berlin = Address("Berlin", "Alexanderplatz")
    address_in_stuttgart = Address("Stuttgart", "Schlossplatz")
    person1 = Person("Sawitzki", "Rainer", address_in_munich) 
    person2 = Person("Musterfrau", "Hannah", address_in_berlin)
    student1 = Student('Einstein', 'Albert', address_in_munich, 'TU')
    worker1 = Worker('Schufter', 'Andrea', address_in_stuttgart, 'Cegos')
    student1.study()
    worker1.work()
    print(student1.say_hello())
    print(worker1.say_hello())
    print(person1.say_hello())
    print(person2.say_hello())
if __name__ == '__main__':
    main()
