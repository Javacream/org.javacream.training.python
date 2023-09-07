class Address:
    def __init__(self, postal_code, city, street):
        self.postal_code = postal_code
        self.city = city
        self.street = street
    def __str__(self):
        return "Address: city=" + self.city + ", street=" + self.street # besser: format()
class Person:
    def __init__(self, lastname, firstname, height, weight, address): # Constructor
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        self.address = address
    def say_hello(self):
        return "Hi, my name is " + self.lastname + ", i live in " + self.address.city


a = Address(81371, 'München', "Marienplatz")
p1 = Person("Sawitzki", "Rainer", 183, 81, a)
p2 = Person("Mustermann", "Andrea", 176, 66, a)

print(a.__str__())
