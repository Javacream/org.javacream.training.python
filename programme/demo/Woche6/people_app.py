from people import *
def main():
    a1 = Address(city='München', street='Marienplatz')
    a2 = Address(city='Berlin', street='Alexanderplatz')
    a3 = Address(city='Stuttgart', street='Schlossplatz')
    c = Company('javacream')
    c.addresses.add(a3)
    c.addresses.add(a1)
    c.addresses.add(a2)
    a3.inhabitants.append(c)
    a2.inhabitants.append(c)
    a1.inhabitants.append(c)
    p1 = Person('H', 'J', 75.9, a1)
    p2 = Person('A', 'B', 95.9, a2)
    s = Student('X', 'Y', 123.55, a3, 'LMU')

    print(p1)
    print(c)
    print(s)
    print(a2)
    
if __name__ == '__main__':
    main()