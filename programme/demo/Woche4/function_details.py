def fn1():
    print('called fn1')
    return "OK"
def fn1():
    print('CHANGED called fn1')
    return "OK"
def fn1(param):
    print('called fn1 with param')
    return "OK"

def main():
    print(fn1())

main()