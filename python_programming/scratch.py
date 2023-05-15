def main():
    def fn1():
        print("executing fn1")
        return "OK from fn1"

    def fn2(p):
        print("executing fn2")
        print(p)
    #fn1()
    name = "Hugo"
    x = fn1
    #print(x)
    #x()
    fn2(name)
    fn2(fn1())#Hier wird der Rückgabewert von fn1 genutzt
    fn2(fn1)#Hier wird fn1 genutzt
    #name() -> Syntax Error, not callable

main()