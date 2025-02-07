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

def main():
    adress_in_munich = Address("München", "Marienplatz")
    person1 = Person("Sawitzki", "Rainer", adress_in_munich) # Implizit: Ein leeres Objekt wird erzeugt und als erster Parameter ergänzt
    person2 = Person("Musterfrau", "Hannah", adress_in_munich) # Implizit: Ein leeres Objekt wird erzeugt und als erster Parameter ergänzt
    person1.adress = adress_in_munich
    print(type(person1))
    print(person1.say_hello()) # Implizit wird person1 in der Methode zum ersten Parameter self
    print(person2.say_hello())
if __name__ == '__main__':
    main()
