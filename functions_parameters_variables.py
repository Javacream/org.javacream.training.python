

def fn1():
    var_fn1 = 42
    print(var_fn1)
   # print(name)
def fn2():
    var_fn2 = 4711    
    print(var_fn2)
   # print(var_fn1)  # Laufzeitfehler, var_fn1 ist hier nicht bekannt!
   # print(name)


def main():
    name = "Hugo"
    fn1()
    fn2()

main()