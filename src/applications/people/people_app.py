from people_service import Person, Student
from address import Address
def main():
    p1 = Person('Sawitzki', 'Rainer') # __init__(self, lastname, firstname), self wird aber intern gesetzt!
    print(p1.say_hello())
    p2 = Person('Meier', 'Hannah') # __init__(self, lastname, firstname), self wird aber intern gesetzt!
    print(p2.say_hello())
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    with open ('address.infos.txt', 'at', encoding='utf-8') as file:
        file.write(f'{a1.info()}\n')
        file.write(f'{a2.info()}\n')
    s1 = Student('Einstein', 'Alberta', 'LMU')
    print(s1.say_hello())
    print(s1.study())

if __name__ == '__main__':
    main()