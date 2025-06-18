# import people
from people import Person, Address, Worker, Student

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', 76.6, 183)
    p2 = Person('Musterperson', 'Hannah', 66.6, 176)
    p3 = Person('Eg', 'Al', 96.6, 186)
    p1.addresses.append(a1)
    p1.addresses.append(a2)
    p2.addresses.append(a2)

    s = Student('Einstein', 'Albert', 77, 163, 'LMU')
    s.addresses.append(a1)
    print(s.study())
    
    w = Worker('Schufter', 'Hannah', 87, 193, 'Javacream')
    w.addresses.append(a2)
    print(w.work())

    print('done')

if __name__ == '__main__': 
    main()