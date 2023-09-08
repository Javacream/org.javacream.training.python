def demo(list, fn):
    for element in list:
        fn(element)


def myfunc(p):
    print(p)

names = ["Hugo", "Emil"]

demo(names, myfunc)