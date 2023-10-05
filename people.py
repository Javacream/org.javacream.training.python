class Person:
    pass

def main():
    def info_fn(obj):
        return "Hello, my name is " + obj.name
    p1 = Person()
    p2 = Person()
    print(type(p1), type(p2))
    p1.name = "Goo"
    p2.name = "Foo"
    p1.info = info_fn
    p2.info = info_fn
    #print(p1.name, p2.name)
    print(p1.info(p1), p2.info(p2))
main()