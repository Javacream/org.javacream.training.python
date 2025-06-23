import requests

NAUTOBOT_URL = 'https://demo.nautobot.com/graphql/'
API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
headers = {
    'Authorization': f'Token {API_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# GraphQL-Query
query = """
{
  devices {
    name
    device_type {
      model
    }
    site {
      name
    }
    status {
      value
    }
  }
}
"""

response = requests.post(NAUTOBOT_URL, json={"query": query}, headers=headers)

# Ergebnis anzeigen
if response.status_code == 200:
    data = response.json()
    for device in data["data"]["devices"]:
        print(f"Name: {device['name']}, Modell: {device['device_type']['model']}, Standort: {device['site']['name']}")
else:
    print(f"Fehler: {response.status_code}")
    # print(response.text)