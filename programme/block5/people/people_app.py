from people import Person, Address, Student
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', 183, 75.9)
    p2 = Person('Musterperson', 'Hannah', 173, 55.9)

    p1.addresses.add(a1)
    p1.addresses.add(a2)
    p2.addresses.add(a2)
    print(p1.addresses)

    s = Student('Einstein', 'Albert', 167, 58.9, 'LMU')
    print(p1.greet())
    print(s.greet())
    s.study()    
main()