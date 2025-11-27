import json

def get_endpoint():
    with open ('config.json') as file:
        config = json.load(file)
        return (config['host'], config['port'])