from people import Person, Address
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', 183, 75.9)
    p2 = Person('Musterperson', 'Hannah', 173, 55.9)

    p1.address = a1
    print(p1.address.city)
    # p1.address = None
    # print(p1.address)
    del p1.address
    # print(p1.address)
main()