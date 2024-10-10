import multiprocessing as mp
import time
import random
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 3))
        print(f'{id} -> {counter}')
        counter += 1
def main():
    proc1 = mp.Process(target=do_something, args=('Proc1', ))
    proc2 = mp.Process(target=do_something, args=('Proc2', ))
    proc1.start()
    proc2.start()
if __name__ == '__main__':
    main()