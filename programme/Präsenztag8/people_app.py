# import people
from people import Person, Address, Worker, Student

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    a3 = Address('München', 'Marienplatz')
    a4 = a1
    p1 = Person('Sawitzki', 'Rainer', 76.6, 183)
    p2 = Person('Musterperson', 'Hannah', 66.6, 176)
    p3 = Person('Eg', 'Al', 96.6, 186)
    p4 = Person('Musterperson', 'Hannah', 66.6, 176)
    p1.addresses.append(a1)
    p1.addresses.append(a2)
    p2.addresses.append(a2)
    s = Student('Einstein', 'Albert', 77, 163, 'LMU')
    s.addresses.append(a1)
    w = Worker('Schufter', 'Hannah', 87, 193, 'Javacream')
    w.addresses.append(a2)
    s1 = 'Hugo'
    s2 = 'Hugo'
    print(a1 == a2)
    print(p1 == p2)
    print(a1 == p1)
    print(p2 == p4)
    print(f'a1 und a3 identisch? {a1 == a3}') # Gleiche Stadt und gleiche Straße sollten dieselbe Adresse sein
    print(a1 == a4) # Vergleich: deuten die Referenzen auf dasselbe Objekt
    print(s1 == s2) # Bisher ist das Ergebnis True nicht nachvollziehbar!!!
    print('done')

if __name__ == '__main__': 
    main()