import time
import random
from multiprocessing import Process
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 5))
        counter += 1
        print(f'{id} -> {counter}')


def main():
    p1 = Process(target=do_something, args=('ID1', ))
    p2 = Process(target=do_something, args=('ID2', ))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()