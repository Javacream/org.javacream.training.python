def Person(lastname, firstname):
    new_object = object() # kann nicht mit neuen Attributen erweitert werden...
    new_object.lastname = lastname
    new_object.firstname = firstname
    return new_object

def main():
    p1 = Person("Sawitzki", "Rainer")
    print(p1.lastname)

main()
