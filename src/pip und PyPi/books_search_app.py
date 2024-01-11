import requests
def main():
    json_response = requests.get('https://openlibrary.org/search.json?q=the+lord+of+the+rings').json()
    print(json_response)

main()    