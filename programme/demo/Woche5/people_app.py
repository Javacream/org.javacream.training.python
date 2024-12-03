from people import Person, Address
def main():
    address = Address(city='München', street='Marienplatz')
    p1 = Person('H', 'J', 75.9)
    p2 = Person('A', 'B', 95.9)
    p1.address = address
    print(p1.say_hello())
    print(p2.say_hello())
    del (p1.address)
    print(p1.say_hello())
    print(p2.say_hello())

if __name__ == '__main__':
    main()