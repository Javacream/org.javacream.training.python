import requests
print(requests.post('http://localhost:8000/api/echo/', json={'message': 'Hello'}).json())