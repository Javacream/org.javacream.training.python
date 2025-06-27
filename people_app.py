from people import Person, Address, Student, Worker
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', a1, a2)
    p2 = Person('Musterperson', 'Hannah', a2)
    s1 = Student('Einstein', 'Albert', 'LMU')
    w1 = Worker('Schufter', 'Johanna', 'Cegos')

    print(p1.introduce())
    print(p2.introduce())
    print(s1.introduce())
    print(s1.study())
    print(w1.work())
    print('done')


if __name__ == '__main__':
    main()