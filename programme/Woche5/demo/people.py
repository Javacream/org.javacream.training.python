class Person:
    def __init__(self, lastname, firstname, address): # Konstruktor
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
        #self.lastname = lastname
        #self.firstname = firstname
        #self.address = address
        super().__init__(lastname, firstname, address)
        self.university = university
    def study(self):
        print(f'ich studiere an {self.university}')    

def main():
    address_in_munich = Address("München", "Marienplatz")
    person1 = Person("Sawitzki", "Rainer", address_in_munich) # Implizit: Ein leeres Objekt wird erzeugt und als erster Parameter ergänzt
    person2 = Person("Musterfrau", "Hannah", address_in_munich) # Implizit: Ein leeres Objekt wird erzeugt und als erster Parameter ergänzt
    student1 = Student('Einstein', 'Albert', address_in_munich, 'TU')
    student1.study()
    print(student1.say_hello())
    print(type(person1))
    print(person1.say_hello()) # Implizit wird person1 in der Methode zum ersten Parameter self
    print(person2.say_hello())
if __name__ == '__main__':
    main()
