import requests
def main():
    new_person = {
        "id": 666,
        "lastname": "Christ",
        "firstname": "Anti",
        "gender": "d",
        "height": 247
    }
    response = requests.put('http://javacream.eu:8080/people', json=new_person)
    print(response.status_code)

    response = requests.delete('http://javacream.eu:8080/people/666')
    print(response.status_code)

if __name__ == '__main__': main()

