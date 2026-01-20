from people_service import Person
def main():
    p1 = Person('Sawitzki', 'Rainer') # __init__(self, lastname, firstname), self wird aber intern gesetzt!
    print(p1.say_hello())
    p2 = Person('Meier', 'Hannah') # __init__(self, lastname, firstname), self wird aber intern gesetzt!
    print(p2.say_hello())

if __name__ == '__main__':
    main()