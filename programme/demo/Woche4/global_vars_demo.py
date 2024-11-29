def fn1():
    global global_var
    global_var = "CHANGED in fn1"
    print(f'in fn1 global_var: {global_var}')

def fn2():
    print(f'in fn2 global_var: {global_var}')

def main():
    local_var = 'def in main'
    print(f'in main global_var: {global_var}, local_var: {local_var}')
    fn1()
    fn2()

global_var = 'Global'

main()

