def fn1():
    height = 183
    print('called fn1')

def fn2(p1:str, p2, p3:list):
    print(p1, p2, p3)
    p1 = "Fridolin" # Neuzuweisung der Referenz p1
    p3.append('orange') # Nutzen des Objektes, auf das p3 zeigt
    return 'OK'

def main():
    fn1()
    name = 'Hugo'
    number = 42
    items = ['banana', 'apple']
    result = fn2(name, number, items)
    print(result)

main()