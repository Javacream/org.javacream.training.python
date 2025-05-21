from people import Person
def main():
    sawitzki = Person('Rainer', 'Sawitzki', 76.6, 1.83)
    print(sawitzki.say_hello())
    print(sawitzki.get_bmi())

    musterperson = Person('Andrea', 'Meier', 56.6, 1.73)
    print(musterperson.say_hello())
    print(musterperson.get_bmi())
    
    print(sawitzki)
main()