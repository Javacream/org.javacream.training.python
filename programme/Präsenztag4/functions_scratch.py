def fn(p1, p2):
    pass

def fn2(params_tuple):
    for param in params_tuple:
        print(param)

def fn3(*params_tuple):
    print(params_tuple)
    for param in params_tuple:
        print(param)

def main():
    fn(1, 9)
    print('################# Normale Funktion Ende')
    fn2([])
    fn2([1])
    fn2([1, 9])
    print('################# List als Parameter Ende')
    print()
    print(1)
    print(1, 9)
    print('################# print mit variabler Parameterliste Ende')
    fn3()
    fn3(1)
    fn3(1, 9)
    print('################# Eigene Varargs Ende')

main()