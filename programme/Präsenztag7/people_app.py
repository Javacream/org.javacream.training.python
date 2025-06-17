# import people
from people import Person, Address

def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    p1 = Person('Sawitzki', 'Rainer', 76.6, 183, a1)
    p2 = Person('Musterperson', 'Hannah', 66.6, 176, a2)
    p3 = Person('Eg', 'Al', 96.6, 186, a1)
    print(p1.lastname)
    print(p2.lastname)
    print(p2.weight)
    print(p3.say_hello())
    print('done')

if __name__ == '__main__': 
    main()