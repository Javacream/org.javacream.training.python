def application():
    list1 = ['A', 'B']

    def fn1(l):
        l.append("C")
        print(l)
    
    fn1(list1)
    print(list1)
    fn1(list1.copy())
    print(list1)


application()