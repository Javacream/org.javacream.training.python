user_input = 'Hugo'

# Wie kann denn die Umwandlungsfunktion 'int' einen Fehler signalisieren?
# Wir tun so, als hätten wir in der Dokumentation gefunden "Wenn Paramter nicht umgewandelt werden kann wird die Zahl -666 zurückgegeben"
number = int(user_input) # Hier wird der ValueError "geworfen" 
if number != -666:
    print(2 * number)
else:
    print(f'{number} kann nicht in eine Zahl konvertiert werden')