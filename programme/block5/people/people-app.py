from people import Person, Address
def main():
    p1 = Person('Sawitzki', 'Rainer', 183, 75.9)
    p2 = Person('Musterperson', 'Hannah', 173, 55.9)
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    print(p1.lastname, p2.lastname)
    print(a1.city, a2.city)

    print(f'{p1.lastname} has a weight of {p1.weight}')
    p1.weight = 77.6
    print(f'{p1.lastname} has now a weight of {p1.weight}')

    p1.eye_color = 'blue'
    print(f'{p1.lastname}: eyes are {p1.eye_color}')
    # print(f'{p2.lastname}: eyes are {p2.eye_color}') # p2 does not have attribute eye_color -> exception

    a3 = a2.copy()
    a3.street = 'somewhere'
    print(a2.street)

main()