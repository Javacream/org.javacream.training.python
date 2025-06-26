from people import Person, Address
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer')
    p2 = Person('Musterperson', 'Hannah')
    p1.addresses.add(a1)
    p1.addresses.add(a2)
    p2.addresses.add(a2)
    print(p1.introduce())
    print(p2.introduce())
    print('done')


if __name__ == '__main__':
    main()