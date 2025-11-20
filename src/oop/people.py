class Person:
    def __init__(self, lastname, firstname, height=170, weight=67):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'

def main():
    person1 = Person('Sawitzki', 'Rainer', 183, 75.8)
    person2 = Person('Muster', 'Hannah', 783, 55.8)
    person3 = Person('Musterperson', 'Andrea')
    person1_dict = {'lastname': 'A', 'firstname': 'B', 'height': 183, 'weight': 75.9}
    person2_dict = {'last': 'A', 'first': 'B', 'h': 183, 'w': 75.9, 'eye_color': 'blue'}

    print(person1.say_hello())
    print(person2.say_hello())
    print('done')

main()
