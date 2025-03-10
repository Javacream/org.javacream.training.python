import requests
def main():
    response = requests.get('https://github.com/Javacream/org.javacream.training.python/tree/deutsche_bahn_netzwerkprogrammierung_26.2.2025')
    # print(response.text)
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data_as_text = response.text
    data = response.json()
    print(data)
if __name__ == '__main__': main()