import json

def write_json_data(path, data):
    with open (path, 'wt', encoding='utf-8') as file:
        json.dump(data, file)
