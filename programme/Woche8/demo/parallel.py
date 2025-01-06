import time
import random
import multiprocessing as mp
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 3))
        print(f'{id} -> {counter}')
        counter += 1
def main():
    process1 = mp.Process(target=do_something, args=('Process 1', ))
    process2 = mp.Process(target=do_something, args=('Process 2', ))
    process1.start()
    process2.start()
if __name__ == '__main__':
    main()