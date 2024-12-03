from people import Person, Address
def main():
    a1 = Address(city='München', street='Marienplatz')
    a2 = Address(city='Berlin', street='Alexanderplatz')
    a3 = Address(city='Stuttgart', street='Schlossplatz')
    p1 = Person('H', 'J', 75.9, a2)
    p2 = Person('A', 'B', 95.9, a1, a2, a3)
    print(p1.say_hello())
    print(p2.say_hello())

if __name__ == '__main__':
    main()