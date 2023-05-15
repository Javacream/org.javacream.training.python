class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def sayHello(self):
        helloMessage = f"Hello, my name is {self.firstname} {self.lastname}"
        if hasattr(self, "address") and self.address:
            helloMessage = f"{helloMessage}, i live in {self.address.city} at {self.address.street}"
        return helloMessage
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
def test():
    p1 = Person("Sawitzki", "Rainer")
    a1 = Address("München", "Marienplatz")
    p1.address = a1

    c1 = Company("Javacream", a1)
    print(p1.sayHello())
    print(c1)    
    print("test done!")

test()