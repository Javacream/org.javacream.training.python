class Person:
    def __init__(self, lastname, firstname, height, weight): # Constructor
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
    # say_hello als Methode ist richtig
    def say_hello(self):
        return "Hi, my name is " + self.lastname

# say_hello als top-level funktion ist strange, aber würde funktionieren
def say_hello(person):
    return "Hi, my name is " + person.lastname

p1 = Person("Sawitzki", "Rainer", 183, 81)
print(p1.lastname)
p2 = Person("Mustermann", "Andrea", 176, 66)
print(p2.lastname)
print(say_hello(p1))
print(p1.say_hello())


