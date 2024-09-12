class Object:
    pass

def read_file():
    with open ('username.csv') as file:
        return file.readlines()

def use_variables():
    rows = read_file()
    splitted = rows[0].split(';')

    user1 = splitted[0]
    id1= splitted[1]
    firstname1=splitted[2]
    lastname1=splitted[3]
    splitted = rows.split(';')
    user2 = splitted[0]
    id2=splitted[1]
    firstname2=splitted[2]
    lastname2=splitted[3]

def use_nested_lists():
    users = []
    for user_info in read_file():
        user = user_info.split(';')
        users.append(user)
    firstname_of_person_2 = users[1][2] # -> firstname des zweiten Users, also 'Laura'
    print(firstname_of_person_2)

def use_list_of_dict():
    users = []
    for user_info in read_file():
        user = dict()
        user['username'] = ""   
        users.append(user)
    users[1]['firstname'] # -> firstname des zweiten Users, also 'Laura'

def use_list_of_object():
    users = []
    for user_info in read_file():
        user = Object()
        user.username = ""
        user.id = ""
        users.append(user)
    users[1].firstname # -> firstname des zweiten Users, also 'Laura'

class Person:
    def __init__(self, username, id, firstname, lastname):
        self.username = username    
        # ...

def use_list_of_object_with_class():
    users = []
    for user_info in read_file():
        user = Person("", "", "", "")
        users.append(user)
    users[1].firstname # -> firstname des zweiten Users, also 'Laura'
