import json
from book import Book
class BookEncoder(json.JSONEncoder):
    def default(self, b):
        return {'isbn': b.isbn, 'title': b.title, 'price': b.price, 'pages': b.pages, 'available':b.available}

def write_dict_to_json_file(file_path, data):
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False, cls=BookEncoder)

def read_dict_from_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if not isinstance(data, dict):
        raise ValueError("The JSON file does not contain a valid dictionary.")

    return data
