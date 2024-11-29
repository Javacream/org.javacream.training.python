import json

with open ('./programme/Woche4/books.json') as json_file:
    data = json.load(json_file)
    print(data)