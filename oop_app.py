from oop import Person, Address, Student

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Musterperson', 'Andrea')
    p2 = Person('Meier', 'Hannah')
    p2.addresses.add(a1)
    a1.people.append(p2)
    p1.lastname = 'Changed'
    print(p1.introduce())
    print(p2.introduce())
    s = Student('Einstein', 'Albert', 'LMU')
    s.addresses.add(a2)
    a2.people.append(s)
    print('done')


if __name__ == '__main__':
    main()