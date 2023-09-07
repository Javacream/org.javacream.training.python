class Address:
    def __init__(self, postal_code, city, street):
        self.postal_code = postal_code
        self.city = city
        self.street = street
    def __str__(self):
        str_template = "Address: postalCode={}, city={}, street={}"
        return str_template.format(self.postal_code, self.city, self.street)
class Person(object): #(object) ist ab Python 3.x Standard, Die Klasse Person erbt von Object
    number_of_eyes = 2
    created_people = 0
    def __init__(self, lastname, firstname, height, weight): # Constructor
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        Person.created_people += 1
    def say_hello(self):
        return "Hi, my name is " + self.lastname
    def __str__(self):
        str_template = "Person: lastname={}, firstname={}, height={}, weight={}"
        return str_template.format(self.lastname, self.firstname, self.height, self.weight)

def select_id():
    return input("enter id, empty id will terminate: ")

class PeopleManager:
    def __init__(self):
        self.people = {}
        self.people_counter = 0
        self.__load_people__()
    def find_by_id(self, id):
        return self.people.get(id)    
    def create(self, lastname, firstname, height=176, weight=81):
        if (type(height) is str):
            height = int(height)
        if (type(weight) is str):
            weight = int(weight)
        self.people_counter = self.people_counter + 1 # shorter: self.people_counter += 1, ++ not in Python
        new_person = Person(lastname, firstname, height, weight)
        self.people[self.people_counter] = new_person
    def __load_people__(self):
        with open("people.txt", "r") as file:
            rows = file.readlines()
            for row in rows:
                if row.endswith('\n'):
                    row = row[0:len(row)-1]
                data =row.split(",")
                self.create(*data)

def execute_search(id):
    people_manager = PeopleManager()
    print(people_manager.find_by_id(id))
def main():
    print(Person.number_of_eyes)
    while(True):
        id = select_id()
        if id in (''):
            break
        execute_search(int(id)) # id is a string, we need a number

#main()


class Student(Person):
    def __init__(self, lastname, firstname, height, weight, uni, city):
        super().__init__(lastname, firstname, height, weight)
        self.university = uni
    def study(self):
        return self.say_hello() + ", i study at " + self.university

p = Person("A", "B", 122, 12)
print(p.say_hello())        
s = Student("Einstein", "Alberta", 188, 177, "TU")
print(s.say_hello())        
print(s.study())        

