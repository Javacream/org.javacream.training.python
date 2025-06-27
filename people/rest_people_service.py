import requests
class PeopleService:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def read_people(self):
        response = requests.get(self.endpoint)
        if response.status_code == 200:
            data = response.json()
            return data
