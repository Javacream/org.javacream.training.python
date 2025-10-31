def fn1():
    message = 'in fn1'
    print(message)
    fn3()
    print(message)

def fn2(param):
    number =9
    print(f'{param}, {number}')

def fn3():
    message = 'in fn3'
    print(message)

def main():
    fn1()
    fn2('Hugo')

main()