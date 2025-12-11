import requests

class PeopleService:
    def __init__(self, endpoint):
        self.endpoint = endpoint
    def get_people(self):
        return requests.get(self.endpoint).json()
