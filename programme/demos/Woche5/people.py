class Person:
    def __init__(self, id, lastname, firstname):  # Der Konstruktor der Klasse Person
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        pass


class Address:
    def __init__(self, param_city, param_street):
        self.city = param_city
        self.street = param_street   

my_list = []  # -> leere Liste mit Literal
my_list = list() # -> leere Liste

# person1 = -> Person mit Literal geht nicht, es gibt kein Personen-Literal
person1 = Person(1, 'Musterperson', 'Andrea') # Der erste Parameter des Konstruktors, als 'self' wird hier nicht angegeben, sondern intern erzeugt
person2 = Person(2, 'Schneider', 'Hannah') # Der erste Parameter des Konstruktors, als 'self' wird hier nicht angegeben, sondern intern erzeugt
print('done')
a = Address('München', 'Marienplatz')