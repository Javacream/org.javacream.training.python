from oop import Person, Address

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Musterperson', 'Andrea', a2)
    p2 = Person('Meier', 'Hannah', a1)
    print(p1.introduce())
    print(p2.introduce())


if __name__ == '__main__':
    main()