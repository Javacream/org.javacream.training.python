import requests

# Konfigurationsparameter
NAUTOBOT_URL = 'http://deine-nautobot-url/api/'
API_TOKEN = 'dein_api_token'

# Header mit API-Token
headers = {
    'Authorization': f'Token {API_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Funktion, um Geräte von Nautobot abzurufen
def get_devices():
    endpoint = 'dcim/devices/'  # Endpunkt für Geräteinformationen
    url = NAUTOBOT_URL + endpoint
    
    try:
        # GET-Anfrage an die API
        response = requests.get(url, headers=headers)
        
        # Überprüfung des Statuscodes
        if response.status_code == 200:
            devices = response.json()
            return devices['results']  # Gibt die Liste der Geräte zurück
        else:
            print(f"Fehler bei der Anfrage: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Es gab einen Fehler: {str(e)}")
        return None

# Hauptprogramm
if __name__ == "__main__":
    devices = get_devices()
    
    if devices:
        print("Geräte in Nautobot:")
        for device in devices:
            print(f"- Name: {device['name']}, Standort: {device['site']['name']}, Modell: {device['device_type']['model']}")
    else:
        print("Keine Geräte gefunden oder Fehler bei der Anfrage.")
