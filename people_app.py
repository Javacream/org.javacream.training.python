from people import Person, Address, Student
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', a1, a2)
    p2 = Person('Musterperson', 'Hannah', a2)
    s1 = Student('Einstein', 'Albert', 'LMU')

    print(p1.introduce())
    print(p2.introduce())
    print(s1.introduce())
    print('done')


if __name__ == '__main__':
    main()