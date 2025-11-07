from people import Person, Address
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', 183, 75.9, a1)
    p2 = Person('Musterperson', 'Hannah', 173, 55.9, a2)
    print(p1.lastname, p2.lastname)

main()