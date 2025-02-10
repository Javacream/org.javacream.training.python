class Person:
    def __init__(self, lastname, firstname, weight, height): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height

    def say_hello(self):
        return f'Hallo, ich bin {self.firstname} {self.lastname}'


def main():
    a_list = list()
    another_list = list()
    a_person = Person('Sawitzki', 'Rainer', 75.3, 183) # a_person ist eine Instanz der Klasse Person
    another_person = Person('Musterperson', 'Hannah', 56.3, 168)
    print(type(a_list))
    print(type(a_person))
    print(a_person.say_hello())
    print(another_person.say_hello())
if __name__ == '__main__':
    main()
