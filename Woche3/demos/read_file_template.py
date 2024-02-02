filename = ""


with open(filename) as file: # with... -> 
    rows = file.readlines() # Ergebnis davon ist eine Liste von strings, in denen jedes Element eine Zeile der Datei ist


# äquivalent zu, aber schlechter Stil, leider in w3school Beispielen genutzt
file = open(filename)
rows = file.readlines() # VORSICHT: Die geöffnete Datei ist zumindest ein paar Sekunden / Minuten nach Ende des Pyhon-Programms immer noch gesperrt!
file.close() # das Schließen verhindert diese Sperre
