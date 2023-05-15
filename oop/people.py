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

class Worker(Person):
    def __init__(self, lastname, firstname, company):
        self.company = company
        super().__init__(lastname, firstname)
    def work(self):
        print(f"a am working at company {self.company}")

def test():
    p1 = Person("Sawitzki", "Rainer")
    a1 = Address("München", "Marienplatz")
    a2 = Address("Berlin", "Alexanderplatz")
    p1.address = a1
    c1 = Company("Javacream", a1)
    w1 = Worker("Schufter", "Hannah", c1)
    w1.address = a2
    print(w1.sayHello())
    w1.work()
test()