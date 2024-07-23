class Object:
    def method3(self):
        pass

def create_person(lastname, firstname):
    obj = Object()
    obj.lastname = lastname
    obj.firstname = firstname
    return obj

def demo_fn():
    print("called demo")

def demo_method(self):
    print(f"called demo, attr1={self.attr1}")


demo = Object()
demo.attr1 = "Hello"
demo.method1 = demo_fn
demo.method3()
demo.method1() # Diese Methode ist nicht gebunden!!! -> Fortgeschrittene Python-Programmierung

Object.method2 = demo_method
demo.method2()

del (Object.method3)    
# demo.method3()



