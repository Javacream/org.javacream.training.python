class Person:
    def __init__(self, lastname, firstname, weight, height, address): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height
        self.address = address

    def say_hello(self):
        return f'Hallo, ich bin {self.firstname} {self.lastname}'
    def __repr__(self):
        return f"Person: lastname={self.lastname}, firstname={self.firstname}, weight={self.weight}, height={self.height}, address={self.address}"

class Student(Person):
    def __init__(self, lastname, firstname, weight, height, address, university):
        super().__init__(lastname, firstname, weight, height, address)
        self.university = university
    def study(self):
        return f'ich studiere an {self.university}'
class Worker(Person):
    def __init__(self, lastname, firstname, weight, height, address, company):
        super().__init__(lastname, firstname, weight, height, address)
        self.company = company
    def work(self):
        return f'ich arbeite bei {self.company}'
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def __repr__(self):
        return f'Address: city={self.city}, street={self.street}'
    def __eq__(self, other):
        if isinstance(other, Address):
           return (self.city.lower() == other.city.lower()) and (self.street.lower() == other.street.lower())
        else:
            return False 
    def __hash__(self):
        return hash(self.city.lower()) + hash(self.street.lower())

def main():
    address_in_munich = Address('München', 'Marienplatz')
    address_in_berlin = Address('Berlin', 'Alexanderplatz')
    student = Student('Einstein', 'Albert', 77.7, 177, address_in_munich, 'TU')
    worker = Worker('Schufter', 'Andrea', 55.5, 161, address_in_berlin, 'Conti')
    print(student.say_hello())
    print(student.study())
    print(worker.say_hello())
    print(worker.work())
if __name__ == '__main__':
    main()
