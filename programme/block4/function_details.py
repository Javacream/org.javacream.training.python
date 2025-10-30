def my_fn(p1):
    print('called my_fn')

def my_fn():
    print('called another my_fn')

def demo(fn):
    fn()

def main():
    name = 'Hugo'
    name = 'Hannah'
    name2 = name
    print(name2)
    my_fn()
    # my_fn('Hugo')
    x = my_fn
    x()
    demo(x)
main()