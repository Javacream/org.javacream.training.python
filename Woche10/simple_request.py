import requests

response = requests.get('http://javacream.eu:8080/people')

#print(type(response.text))
#print(type(response.json()))
for person in response.json():
    #print(type(person))
    print(person["lastname"])