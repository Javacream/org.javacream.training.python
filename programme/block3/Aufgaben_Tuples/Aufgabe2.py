seasons = ('Frühling', 'Sommer', 'Herbst', 'Winter')

index = int(input("Geben Sie den Index der Jahreszeit an: "))

try:
    print(seasons[index- 1])
except:
    print(f"Der eingegebene Index {index} entspricht keiner Jahreszeit")    