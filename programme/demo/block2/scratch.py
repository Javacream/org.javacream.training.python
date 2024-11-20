while True:
    try:
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
    except:
        print('da hat etwas nicht geklappt')
    again = input('nochmal j|n')
    if again == 'n':
        break
