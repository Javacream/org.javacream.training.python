def fn_one_param(p):
    print(p)

def fn_default_param(p1, p2=9):
    print(p1, p2)

#def fn_wrong_default_param(p1, p2=9, p3):
#    print(p1, p2)

def fn_varargs(p, *varargs):
    print(p, varargs)

def fn_varargs_with_keyworded(p, *varargs, p3):
    print(p, varargs, p3)

def main():
    #fn_one_param()
    # fn_one_param(42, 2)
    fn_one_param(42)
    fn_default_param(1,2)
    fn_default_param(1)
    fn_varargs(1)
    fn_varargs(1, 2)
    fn_varargs(1, 2, 3, 4, 5)
    fn_varargs_with_keyworded(1,2, p3='Hugo')
main()