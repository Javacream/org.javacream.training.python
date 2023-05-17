import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.json()[0]["name"])