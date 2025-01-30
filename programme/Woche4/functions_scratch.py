def fn1(fn1_param = 'param for fn1'):
    fn1_var = 'in fn1'
    print(f'var = {fn1_var}, {fn1_param}')

def fn2(fn2_param):
    fn2_var = 'in fn2'
    # print(main_var)
    print(f'var = {fn2_var}, {fn2_param}')

def main():
    main_var = 'Hugo'
    main_var2 = ['A', 'B', 'C']
    fn1()
    fn1('Emil')
    fn1(main_var)
    # fn2()
    fn2(main_var2)

if __name__ == '__main__':
    main()