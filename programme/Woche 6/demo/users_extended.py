def read_file():
    with open ('username_extended.csv') as file:
        return file.readlines()

class Person:
    def __init__(self, username, id, firstname, lastname, active):
        self.username = username    
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.active = True if active == 'active' else False
def users(raw_data):
    users = list()
    user_infos = [row[0:len(row) - 1].split(';') for row in raw_data]
    for user_info in user_infos:
        person = Person(*user_info)
        users.append(person)
    return users

def length(users_list):
    return len(users_list)

def ids(users_list):
    return [p.id for p in users_list]

def sort_by_lastname(users_list: list):
    users_list = users_list.copy()
    users_list.sort(key=lambda p : p.lastname)
    return users_list
def sort_by_id(users_list: list):
    users_list = users_list.copy()
    users_list.sort(key=lambda p : p.id)
    return users_list
def sort_by_username(users_list: list):
    users_list = users_list.copy()
    users_list.sort(key=lambda p : p.username)
    return users_list
def find_active_users(users_list: list):
    return [user for user in users_list if user.active]
def find_inactive_users(users_list: list):
    return [user for user in users_list if not user.active]

def write_result(header, data):
    print(header)
    if isinstance(data, list):
        for element in data:
            if isinstance(element, Person):
                print('\t', element.username, element.id, element.lastname, element.firstname)
            else:
                print('\t', element)    
    else:
        print('\t', data)        
def application():
    users_list = users(read_file())
    users_list_length = length(users_list)
    user_ids = ids(users_list)
    users_sorted_by_id = sort_by_id(users_list)
    users_sorted_by_username = sort_by_username(users_list)
    users_sorted_by_lastname = sort_by_lastname(users_list)
    active_users = find_active_users(users_list)
    inactive_users = find_inactive_users(users_list)
    write_result('Length:', users_list_length)
    write_result('Ids:', user_ids)
    write_result('By id:', users_sorted_by_id)
    write_result('By username:', users_sorted_by_username)
    write_result('By lastname:', users_sorted_by_lastname)
    write_result('Active:', active_users)
    write_result('Inactive:', inactive_users)
    print("done")
    
application()