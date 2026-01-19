name = 'Hugo'

def fn1():
    global name
    print(f'in fn1: {name}')
    name = 'Emil'
    print(f'in fn1 after change: {name}')
def fn2():
    print(f'in fn2: {name}')

def main():
    fn1()
    fn2()

main()