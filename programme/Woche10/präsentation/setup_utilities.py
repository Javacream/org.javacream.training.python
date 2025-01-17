def names_from_people_list(people_dict_list):
    return [f"{person['firstname']}.{person['lastname']}" for person in people_dict_list]

def directories_from_path(path):
    names = path.split('/')
    directories = []
    directories.append(names[0])
    for i in range(1, len(names)):
        directories.append(f"{directories[i-1]}/{names[i]}")
    return directories    
