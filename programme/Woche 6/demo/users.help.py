def read_file():
    with open ('username.csv') as file:
        return file.readlines()

class Person:
    def __init__(self, username, id, firstname, lastname):
        self.username = username    
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
def users(raw_data):
    users = list()
    user_infos = [row[0:len(row) - 1].split(';') for row in raw_data]
    for user_info in user_infos:
        person = Person(*user_info)
        users.append(person)
    return users

def application():
    users_list = users(read_file())
    print("done")
    
application()