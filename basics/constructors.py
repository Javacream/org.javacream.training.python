class Person:
    def __init__ (new_object, lastname, firstname):
        new_object.lastname = lastname
        new_object.firstname = firstname

def main():
    p1 = Person("Sawitzki", "Rainer")
    print(p1.lastname)

main()
