from people import Person, Address

def main():
    p1 = Person(42, "Meier", "Hans")
    p2 = Person(4711, "Schneeider", "Hanna")
    a = Address('München', 'Marienplatz')
    p1.address = a
    print(p1.say_hello())
    print(str(p1))

if __name__ == "__main__":
    main()