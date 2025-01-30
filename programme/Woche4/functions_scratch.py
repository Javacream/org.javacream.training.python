def fn1():
    fn1_var = 'in fn1'
    print(f'var = {fn1_var}')

def fn2():
    fn2_var = 'in fn2'
    # print(main_var)
    print(f'var = {fn2_var}')

def main():
    main_var = 'Hugo'
    main_var2 = ['A', 'B', 'C']
    fn1()
    fn2()

if __name__ == '__main__':
    main()