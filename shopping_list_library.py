def read_raw_shopping_list(path):
    with open (path) as file:
        raw_items = file.readlines()
    return raw_items

def get_raw_shopping_list(raw_items):
    items = list()
    return [raw_item[0:-1] if raw_item.endswith('\n') else raw_item for raw_item in raw_items]

def get_items(path):
    data = read_raw_shopping_list(path)
    return get_raw_shopping_list(data)

def get_unique_items(items):
    unique_items = set(items)
    return unique_items

def create_shopping_list(items):
    shopping_list = dict()
    unique_items = get_unique_items(items)
    for item in unique_items:
        shopping_list[item] = items.count(item)
    return shopping_list

def write_shopping_list_to(path, shopping_list):
    with open (path, 'wt') as file:
        for item in shopping_list:
            file.write(f'{item}: {shopping_list[item]}\n')
