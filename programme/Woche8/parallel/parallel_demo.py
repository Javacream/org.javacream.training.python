import time
import random

def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 5))
        counter += 1
        print(f'{id} -> {counter}')

def caller(callback_function, arg):
    print(f'calling  {callback_function} with arg {arg}')
    callback_function(arg)

def main():
    caller(do_something, 'ID1')
    do_something('ID2')


if __name__ == '__main__':
    main()