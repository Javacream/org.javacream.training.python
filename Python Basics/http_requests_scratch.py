import requests

url = 'http://javacream.eu:8081/api/books/ISBN2'
result = requests.get(url)
# text = result.text
data = result.json()
print(data['title'])