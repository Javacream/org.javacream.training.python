from people import *
if (__name__ == '__main__'):
    p1 = Person("Mustermann", "Hans")
    p2 = Person("Meier", "Hanna")
    p3 = Person("Schneider", "Angela")

    p1.marry(p2)
    try:
        p3.marry(p2)
        print("ERROR, p3 must not be able to marry p2")
    except:
        print("ok, p3 cannot marry p2")
    try:
        p3.divorce()
        print("ERROR, p3 must not be married")
    except:
        print("ok, p3 cannot divorce, is not married")

    p2.divorce()
    p3.marry(p2)


