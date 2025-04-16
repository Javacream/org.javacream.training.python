class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def say_hello(self):
        return "Hello!"
    def greet(self, friendly):
        if friendly:
            return f"Hi, my name is {self.name}"
        else:
            return f"Good day, my name is {self.name}"
def main():
    a1 = Address("München", "Marienplatz")
    a2 = Address("Berlin", "Alexanderplatz")
    person1: Person = Person("Sawitzki", 183, 75.7)
    person2 = Person("Meier", 189, 83.5)
    person1.addresss = a1
    print("done")
main()