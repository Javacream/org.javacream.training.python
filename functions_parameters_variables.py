

def fn1():
    var_fn1 = 42
    print(var_fn1)
   # print(name)
def fn2():
    var_fn2 = 4711    
    print(var_fn2)
   # print(var_fn1)  # Laufzeitfehler, var_fn1 ist hier nicht bekannt!
   # print(name)

def fn3(param):
    print(param)

def main():
    name = "Hugo"
    fn1()
    fn2()
    # fn3() # fehlender Übergabeparameter
    # param = 42 fn3(), nur konzeptuell, syntaktisch nicht korekt und überflüssig!
    fn3(42) # korrekt, implizit wird hier vor dem Eintritt in die function fn3 param=42 gesetzt
    fn3(name) # korrekt, implizit wird hier vor dem Eintritt in die function fn3 param=name gesetzt

main()