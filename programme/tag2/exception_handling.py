height = input("Körpergröße?")
try:
    print("Versuch der Umwandlung")
    height = int(height)
    print(f"{height} ist als Zahl interpretierbar")
except Exception as e:
    print(f"{height} ist nicht als Zahl interpretierbar: {e}")