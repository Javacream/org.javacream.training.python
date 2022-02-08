counter = 0
people = {}
def create_person(lastname, firstname):
    global counter
    counter = counter + 1
    person = (counter, lastname, firstname)
    people[counter] = person
    return counter
def find_person_by_id(id):
    return people.get(id)   

if __name__ == "__main__":
    print ("executing as main")
else:
    print ("imported as " + __name__)


