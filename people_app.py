from people import Person, Address
def main():
    a1 = Address('München', 'Marienplatz')
    p1 = Person('Sawitzki', 'Rainer', a1)
    p2 = Person('Musterperson', 'Hannah', a1)
    print(p1.introduce())
    print(p2.introduce())
    print('done')


if __name__ == '__main__':
    main()