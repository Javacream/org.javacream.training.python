class Person:
    def __init__(self, lastname, firstname): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        greeting = f'Hallo, mein Name ist {self.firstname} {self.lastname}'
        return greeting

def main():
    person1 = Person("Sawitzki", "Rainer") # Implizit: Ein leeres Objekt wird erzeugt und als erster Parameter ergänzt
    person2 = Person("Musterfrau", "Hannah") # Implizit: Ein leeres Objekt wird erzeugt und als erster Parameter ergänzt
    print(type(person1))
    print(person1.say_hello()) # Implizit wird person1 in der Methode zum ersten Parameter self
    print(person2.say_hello())
if __name__ == '__main__':
    main()
