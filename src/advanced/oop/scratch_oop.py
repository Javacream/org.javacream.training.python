class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def say_hello(self):
        print(self.lastname)

def my_func(x):
    print("my_func")
p1 = Person("A", "B")

p2 = Person("C", "D")

# p1.say_hello()
# p2.say_hello()
Person.abc = my_func

p2.abc()
p1.abc()


class Object:
    pass 

p2.__class__ = Object
print(p2.__class__)
print(dir(p2))
print(p2.say_hello())