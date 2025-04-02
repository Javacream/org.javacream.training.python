height = input("Körpergröße?")
try:
    height = int(height)
    print(f"{height} ist als Zahl interpretierbar")
except:
    print(f"{height} ist nicht als Zahl interpretierbar")