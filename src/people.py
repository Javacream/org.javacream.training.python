class Person:
    # constructor
    def __init__(self, lastname, firstname, height):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'

def main():
    person1 = Person('Sawitzki', 'Rainer', 183)
    person2 = Person('Musterfrau', 'Hannah', 177)

    print(person1.say_hello(), person2.say_hello())
    print(type(person1), type(person2))

main()