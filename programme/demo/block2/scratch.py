while True:
    try:
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        print (n1 + n2 / n3)
    except Exception as e:
        print(f'da hat etwas nicht geklappt: {e}')
    again = input('nochmal j|n')
    if again == 'n':
        break
