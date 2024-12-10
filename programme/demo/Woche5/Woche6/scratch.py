def complex_functional(callback):
    print('entering')
    print(callback())
    print('exiting')

def fn1():
    return "i am fn1"    
def fn2():
    return "i am fn2"    

def main():
    complex_functional(fn1)
    complex_functional(fn2)

if __name__ == '__main__':
    main()