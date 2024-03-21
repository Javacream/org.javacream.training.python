import requests

host = "javacream.eu"
port = 8080
endpoint = f"http://{host}:{port}/people"

response = requests.get(endpoint)

#print(type(response.text))
#print(type(response.json()))
for person in response.json():
    #print(type(person))
    print(person["lastname"])