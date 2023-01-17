class A:
    def __init__(self):
        print("########## init A")
        self.a = "A"

    def get_a(self):
        return self.a
    

class B:
    def __init__(self):
        print("########## init B")
        self.b = "B"
    def get_b(self):
        return "self.b"
class C:
    def get_c(self):
        return "self.c"
class D:
    def get_d(self):
        return "self.d"


class Demo(B, A, D, C):
    def __init__(self):
        print("########## init Demo")
        self.demo = "Demo"
        #super().__init__()
        B.__init__(self)
        A.__init__(self)

d = Demo()
print(dir(Demo))
print(dir(d))
