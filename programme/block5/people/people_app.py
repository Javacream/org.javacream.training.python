from people import Person, Address

def main():
    p1 = Person('Sawitzki', 'Rainer', 183, 76.2)
    p2 = Person('Musterperson', 'Hannah', 179, 66.2)
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')


    print(p1.lastname, p2.lastname)
    print(a1.city, a2.city)

    p1.weight = 75.8
    print(p1.weight)

    p1.eye_color = 'blue'
    print(p1.eye_color)
    # print(p2.eye_color) # error: p2 has no attribute eye_color



main()
