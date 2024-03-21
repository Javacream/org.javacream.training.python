import requests 
import json
host = "javacream.eu"
port=8080
endpoint = f"http://{host}:{port}/people"

def find_by_id(id):
    return requests.get(f"{endpoint}/{id}").json()

def find_all():
    return requests.get(f"{endpoint}").json()

def delete_by_id(id):
    return requests.delete(f"{endpoint}/{id}").status_code

def create_person(person):
    json_data = json.dumps(person)
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post(endpoint, data=json_data, headers=headers)

        if response.status_code == 200:
            return "OK"
        else:
            return f"Error: {response.status_code}"

    except requests.exceptions.RequestException as e:
        print("an error occurred:", e)

def update_person(person):
    json_data = json.dumps(person)
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.put(endpoint, data=json_data, headers=headers)

        if response.status_code == 200:
            return "OK"
        else:
            return f"Error: {response.status_code}"

    except requests.exceptions.RequestException as e:
        print("an error occurred:", e)
