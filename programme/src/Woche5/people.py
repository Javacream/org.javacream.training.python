class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
class Person:
    def __init__(self, name, height, weight, address):
        self.name = name
        self.height = height
        self.weight = weight
        self.address = address
    def say_hello(self):
        return "Hello!"
    def greet(self, friendly):
        if friendly:
            return f"Hi, my name is {self.name}"
        else:
            return f"Good day, my name is {self.name}"
class PeopleService:
    def __init__(self):
        self.people = set()
    def add(self, person:Person):
        self.people.add(person)
    def find_by_height(self, height):
        return [p for p in self.people if p.height == height]
    