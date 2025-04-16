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
    person1 = Person("Sawitzki", 183, 75.7)
    person2 = Person("Meier", 189, 83.5)
    person1.name = "Mustermann"
    person1.given_name = "Hugo"
    print("done")
main()