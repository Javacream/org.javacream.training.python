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
    print(person1.name)
    person1.name = "Musterperson"
    print(person1.name)
    print(person1.say_hello())    
    print(person2.say_hello())
    print(person1.greet(True))    
    print(person2.greet(False))
main()