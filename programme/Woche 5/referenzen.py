def application():
    list1 = ['A', 'B']

    def fn1(l):
        l.append("C")
        print(l)

    def fn2(l):
        l = ['A', 'B', 'C', 'D']
        print(l)


    fn1(list1) # implizit: l = list1
    print(list1)
    fn2(list1)
    print(list1)
application()