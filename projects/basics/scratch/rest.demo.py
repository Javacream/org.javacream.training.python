import requests

endpoint_url = "http://h2908727.stratoserver.net:8080/api/books"

response = requests.get(endpoint_url)
#todo: response-Http-Status, 200 OK
print(response)#der Beginn der Antwort vom Server
#todo: JSON-Decoder von Pythone wirft eine Exception, falls eine Umwandlung in Python list/dict nicht möglich ist
result = response.json()
print(result)
print(type(result))
print(type(result[0]))
#todo: Result ist list/dict, damit ist das Auslesen der Daten auf die dict-Syntax beschränktprint(result[0]['title'])
print(result[0]['title'])
#durchaus sinnvoll: Umwandlung des Dictionaries in ein Objekt -> book.title, kann auch generisch erfolgen
#diskussionswürdig: Umwandlung in eine Instanz der Klasse "Book" 
