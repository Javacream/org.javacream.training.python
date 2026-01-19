import requests

def main():
    url = "http://javacream.eu:8080/people"

    response = requests.get(url)

    print("Status code:", response.status_code)
    print("Raw response:", response.text)
    people = response.json()
    print(people)
main()