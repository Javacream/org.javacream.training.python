from oop import Person, Address

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Musterperson', 'Andrea')
    p2 = Person('Meier', 'Hannah')
    p2.address = a1
    p1.lastname = 'Changed'
    print(p1.introduce())
    print(p2.introduce())


if __name__ == '__main__':
    main()