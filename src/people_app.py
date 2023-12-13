import people
import datetime

def main():
    address = people.Address('München', 81371, 'Marienplatz')
    person1 = people.Person('Sawitzki', 'Rainer', 183, address)
    person2 = people.Person('Musterfrau', 'Hannah', 177, address)

    print(person1.say_hello(), person2.say_hello())
    print(type(person1), type(person2))

    x = datetime.datetime.now()
    print(x)

main()