def do_something():
    print('doing something')

do_something()

def do_something(p):
    print(f'doing something completely different with {p}')

do_something(True)

name = 'Sawitzki'
name = 'Musterperson'

x = do_something
x(42)

def decorate(fn):
    print('before')
    fn('Hugo')
    print('after')


def main():
    message = 'Hello'
    def inner_function():
        print('inner function')
    inner_function()
    decorate(do_something) 
main()