def fn1():
    height = 183
    print('called fn1')
def fn2(p1:str, p2, p3:list = ['Default']):
    print(p1, p2, p3)
    p1 = "Fridolin" # Neuzuweisung der Referenz p1
    p3.append('orange') # Nutzen des Objektes, auf das p3 zeigt
    return 'OK'

def fn3(*args):
    print(args)

def fn4(**kwargs):
    print(kwargs)

def main():
    name = 'Hugo'
    number = 42
    items = ['banana', 'apple']
    fn4()
    fn4(name= 'Hugo', number= 9)
    fn4(name= 'Hugo')
if __name__ == '__main__':
    main()