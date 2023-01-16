#class Person:
    #lastname, firstname


#class Person(lastname, firstname)

def my_func(x):
    print(x.lastname)

class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.say_hello_as_attribute = my_func
    def say_hello(self):
        print(self.lastname)

p = Person("Sawitzki", "Rainer")
p.say_hello_as_attribute(p)
p.say_hello()

Person.say_hello(p)
print(dir(Person))

class Object:
    pass
o = Object()
o.lastname = "Hugo"
Person.say_hello(o)
