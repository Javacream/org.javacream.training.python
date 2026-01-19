# Bestimmung des aktuellen Datums & Uhrzeit

# Das Modul datetime steht als Objekt datetime zur Verfügung
import datetime

print(datetime)
print(datetime.datetime.now())

# Das Modul datetime steht als Objekt dt zur Verfügung
import datetime as dt

print(dt)
print(dt.datetime.now())

# Das Objekt datetime des Moduls datetime steht zur Verfügung
from datetime import datetime # bevorzugte Variante in der Python-Community

print(datetime)
print(datetime.now())

# Das Objekt datetime des Moduls datetime steht unter dem Namen dt zur Verfügung
from datetime import datetime as dt

print(dt)
print(dt.now())

