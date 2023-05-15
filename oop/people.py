class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def sayHello(self):
        helloMessage = f"Hello, my name is {self.firstname} {self.lastname}"
        return helloMessage
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

def test():
    p1 = Person("Sawitzki", "Rainer")
    a1 = Address("München", "Marienplatz")
    p1.address = a1
    print("test done!")

test()