while True:
    value = input('Gib eine Zahl ein: ')
    try:
        number = float(value)
        print(number)
    except:
        print(f'{value} kann nicht als Zahl interpretiert werden')    