from people import Person, Address, Student

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', 183, 76.2, a1)
    p2 = Person('Musterperson', 'Hannah', 179, 66.2, a2)
    p3 = Person('Schufter', 'Hans', 199, 96.2, a2)


    print(p1.lastname, p2.lastname)
    print(a1.city, a2.city)

    p1.weight = 75.8
    print(p1.weight)

    p1.eye_color = 'blue'
    print(p1.eye_color)
    # print(p2.eye_color) # error: p2 has no attribute eye_color

    p2.address.street = 'Ostbahnhof'
    print(p2.address.street, p3.address.street)

    print(type(p1), type(a1))

    s1 = Student('Einstein', 'Albert', 169, 65.5, a1)
main()
