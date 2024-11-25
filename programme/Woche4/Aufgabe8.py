import json

#books = [{"isbn":"ISBN1","title":"Java","price":9.99,"available":True},{"isbn":"ISBN2","title":"Spring","price":19.99,"available":True},{"isbn":"ISBN3","title":"HTML5","price":4.99,"available":True},{"isbn":"ISBN4","title":"React","price":19.99,"available":True},{"isbn":"ISBN5","title":"Docker","price":29.99,"available":True}]
#print("done")

with open ('./programme/Woche4/books.json') as json_file:
    data = json.load(json_file)
    print(data)