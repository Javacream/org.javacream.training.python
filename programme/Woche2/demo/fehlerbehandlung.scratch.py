try:
    value = int("42")
    value = int("666")
    value = int("Egal")
    value = int("666")
except Exception as e: # Exception as e -> bitte aktuell akzeptieren, zum Verstehen brauchen wir OOP -> Woche 5
    print(f'Fehleingabe, Grund {e}')