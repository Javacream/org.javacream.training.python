import json

def read_configuration(path):
    with open(path, 'r') as file:
        config = json.load(file)
    return config   