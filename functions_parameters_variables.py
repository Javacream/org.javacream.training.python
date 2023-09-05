name = "Hugo"

def fn1():
    global name
    name = "Emil"
    var_fn1 = 42
    print(var_fn1)
    print(name)
def fn2():
    var_fn2 = 4711    
    print(var_fn2)
    # print(var_fn1)  # Laufzeitfehler, var_fn1 ist hier nicht bekannt!
    print(name)

fn1()
fn2()

