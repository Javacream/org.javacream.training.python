import requests

# URL des RESTful WebService
url = "http://javacream.eu:8080/api/books"

# GET-Anfrage senden
response = requests.get(url)

# Statuscode überprüfen, um sicherzustellen, dass die Anfrage erfolgreich war
if response.status_code == 200:
    # Daten im JSON-Format extrahieren
    data = response.json()
    
    # Ausgabe der Daten
    print("Daten erfolgreich empfangen:")
    for element in data:
        print(f"{element}")
else:
    print(f"Fehler bei der Anfrage: {response.status_code}")

