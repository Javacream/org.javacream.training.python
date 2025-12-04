import requests
def main():
    response = requests.get('http://javacream.eu:8080/people')
    person_text = response.text
    print(person_text)
    person_dict = response.json()
    print(person_dict)
if __name__ == '__main__': main()