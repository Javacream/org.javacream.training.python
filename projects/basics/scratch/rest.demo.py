import requests

endpoint_url = "http://h2908727.stratoserver.net:8080/api/books"

response = requests.get(endpoint_url)
print(response)#der Beginn der Antwort vom Server
result = response.json()
print(result)