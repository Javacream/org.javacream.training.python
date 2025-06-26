from people import Person
def main():
    p1 = Person('Sawitzki', 'Rainer')
    p2 = Person('Musterperson', 'Hannah')
    print(f'the first person is named {p1.firstname} {p1.lastname}')
    print(f'the second person is named {p2.firstname} {p2.lastname}')
    print('done')


if __name__ == '__main__':
    main()