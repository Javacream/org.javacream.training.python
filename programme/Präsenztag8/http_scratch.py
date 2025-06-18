# with open ('http-url') so geht's nicht! Dafür gibt es keine BuiltIn-Funktion
# import socket viel zu kompliziert, der HTTP-Standard wird hier nicht genutzt

# Besser
# Recherche über http-Bibliotheken in Python, Ergebnis ist z.B die Bibliothek requests
# Vorsicht: Diese ist kein Core-Modul
# import requests -> Modul nicht gefunden
# pip install requests

import requests

def main():
    response = requests.get('http://javacream.eu:8080/people')
    print(response.status_code)
    print(type(response.text))
    print(type(response.json()))
    people_data_list = response.json()
    print('done')
 
if __name__ == '__main__':
    main()