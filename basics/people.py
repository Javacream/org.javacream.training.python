class Person:
    def __init__(self, lastname, firstname, weight, address):
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.address = address
    def say_hello(self):
        return f"Hello, my name is {self.lastname}"
    def __repr__(self):
        return f"Person: lastname={self.lastname}, firstname={self.firstname}"

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def __repr__(self):
        return f"Address: city={self.city}, street={self.street}"

def main():
    a1 = Address("München", "Marienplatz")
    a2 = Address("Hamburg", "Reeperbahn")
    p1 = Person("Sawitzki", "Rainer", 75, a1)
    p2 = Person("Müller", "Hannah", 56, a2)
    p3 = Person("Meier", "Andrea", 96, a2)
    p1_as_list = list(["Sawitzki", "Rainer", 75, a1])
 
    print(f"der nachname von p1 ist {p1.lastname}")
    print(f"der nachname von p1_as_list ist {p1_as_list[0]}")

    print(p1)
    print(p1.say_hello())
    print("people done")


main()