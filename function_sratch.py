def fn_varargs(*args):
    #print(type(args))
    #print(len(args))
    for p in args:
        print(p)

def fn_keywordedargs(**kwargs):
    #print(type(kwargs))
    #print(len(kwargs))
    for key in kwargs:
        print(type(key))



#fn_varargs(1,True,"Hugo",[1,2])
fn_keywordedargs(lastname= "Sawitzki", firstname="Rainer")