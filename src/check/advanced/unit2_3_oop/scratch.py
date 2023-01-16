class A:
    def sayhi(self):
        print("A")


class B:
    def sayhi(self):
        print("B")


class M(B, A):
    def sayhi(self):
        super().sayhi()
        B.sayhi(self)
        A.sayhi(self)
        print("M")

m = M()
m.sayhi()

print(M.__mro__)
print(m.__class__.__mro__)
print(M.mro())

class Mixin_1:
    def __init__(self):
        self.member = "Hugo"
        print("################## Hugo")
        print(f"################## {self.member}")
    def x(self):
        print(self.member)    

class Mixin_2:
    def __init__(self):
        self.member = "Emil"
        print("################## Emil")
        print(f"################## {self.member}")

class D(Mixin_2, Mixin_1, A, B):
    def __init__(self):
        super().__init__()
        print(f"################## {self.member}")
        Mixin_1.__init__(self)
        print(f"################## {self.member}")
    def do_it(self):
        print(self.member)  
        Mixin_1.x(self)
    def do_it2(self):
        print(self)  

d = D()
d.do_it()

print(type(d))

D.do_it2("Hu")