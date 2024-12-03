from people import Person
def main():
    p1 = Person('H', 'J', 75.9)
    p2 = Person('A', 'B', 95.9)
    print(p1.say_hello())
    print(p2.say_hello())

if __name__ == '__main__':
    main()