def fn1():
    print('called fn1')

def fn2(p1, p2):
    print(p1, p2)
    return 'OK'

def main():
    fn1()
    result = fn2('Hugo', 42)
    print(result)

main()