# python 3.x
# pip install requests
import requests
def main():
    book = {'isbn': 'ISBN1', 'title': 'java in action', 'price': 1.99, 'available': False}
    response = requests.put('http://javacream.eu:8081/api/books/ISBN1', json=book)
    if response.ok:
        data = response.json()
        print(data)
    print(data)
if __name__ == '__main__': main()