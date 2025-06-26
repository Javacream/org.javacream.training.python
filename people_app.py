from people import Person
def main():
    p1 = Person('Sawitzki', 'Rainer')
    p2 = Person('Musterperson', 'Hannah')
    print(p1.introduce())
    print(p2.introduce())
    print('done')


if __name__ == '__main__':
    main()