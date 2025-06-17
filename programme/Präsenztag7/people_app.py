# import people
from people import Person

def main():
    p1 = Person('Sawitzki', 'Rainer', 76.6, 183)
    p2 = Person('Musterperson', 'Hannah', 66.6, 176)
    p3 = Person('Eg', 'Al', 96.6, 186)
    print(p1.lastname)
    print(p2.lastname)
    print(p2.weight)
    print('done')

if __name__ == '__main__': 
    main()