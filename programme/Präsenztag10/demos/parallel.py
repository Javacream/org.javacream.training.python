import time
import random
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 5))
        counter += 1
        print(f'{id} -> {counter}')


def main():
    do_something('ID-1')
    do_something('ID-2')
if __name__ == '__main__':
    main()