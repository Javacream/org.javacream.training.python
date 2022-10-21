from urllib import response

import requests

response = requests.post("http://h2908727.stratoserver.net:8080/api/books/Egal?price=1.99")
if (response.status_code == 200):
    print("success")
else:
    print(f"error: {response.status_code}")

