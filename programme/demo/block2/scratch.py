while True:
    try:
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
    except Exception as e:
        print(f'da hat etwas nicht geklappt: {e}')
    again = input('nochmal j|n')
    if again == 'n':
        break
