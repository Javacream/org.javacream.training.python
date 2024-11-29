def fn_with_param(p1, *args, p2): # Variable Parameterliste, 'varargs'
    print(f'p1={p1}')
    for arg in args:
        print(arg)

def main():
    fn_with_param('P1', "P2")
    fn_with_param('One', 'Two', 'Three')
main()