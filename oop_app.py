from oop import Person

def main():
    p1 = Person('Musterperson', 'Andrea')
    p2 = Person('Meier', 'Hannah')
    print(p1.introduce())
    print(p2.introduce())


if __name__ == '__main__':
    main()