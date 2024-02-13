class Person:
    def __init__(self, lastname, firstname, weight): # "Der Konstruktor der Klasse"
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
    def introduce(self):
        return f"Hello, i am {self.firstname} {self.lastname}"


def main():
    person_sawitzki = Person("Sawitzki", "Rainer")
    mustermann = Person("Mustermann", "Hannah")

    print(person_sawitzki.introduce())
    print(mustermann.introduce())
main()