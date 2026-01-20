from people_service import Person
from address import Address
def main():
    p1 = Person('Sawitzki', 'Rainer') # __init__(self, lastname, firstname), self wird aber intern gesetzt!
    print(p1.say_hello())
    p2 = Person('Meier', 'Hannah') # __init__(self, lastname, firstname), self wird aber intern gesetzt!
    print(p2.say_hello())
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    print(a1.info())
    print(a2.info())
if __name__ == '__main__':
    main()