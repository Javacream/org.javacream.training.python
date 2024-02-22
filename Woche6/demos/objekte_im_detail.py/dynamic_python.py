name = "Hugo"
message = "Hello"

message.capitalize

print(type(name))
print(type(message))


class Person:
    def __init__(self, lastname):
        self.lastname = lastname

    def say_hello(self):
        return f"Hello, my name is {self.lastname}"


def main():
    p1 = Person("Sawitzki")
    p2 = Person("Musterfrau")
    print(p1.say_hello())
    print(p2.say_hello())

    p1.firstname = "Rainer"
    print(p1.firstname)
    #print(p2.firstname)

    Person.number_of_eyes = 2
    print(p1.number_of_eyes)

    def demo(self):
        print(self.lastname)

    Person.demo_method = demo

    p1.demo_method()
main()