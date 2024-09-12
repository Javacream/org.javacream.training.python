import person as p

def fn1():
    print("Hugo")
def fn2(self):
    print(self)

def application():
    p1 = p.Person("a", 1, 'b', 'c', 'active')
    p2 = p.Person("b", 2, 'e', 'f', 'inactive')
    print(type(p1))
    p1.hugo = fn1
    p1.hugo()
    p1.demo_attr = 42
    print(p1.demo_attr)
    p.Person.emil = fn2
    p1.emil()
    p2.emil()
application()