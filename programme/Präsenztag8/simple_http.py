import requests

def main():
    data = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    print(data)
 
if __name__ == '__main__':
    main()