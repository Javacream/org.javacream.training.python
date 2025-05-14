import random
import time
from multiprocessing import Process
def do_something(id):
    counter = 0
    while True:
        rand = random.randint(1, 5)
        time.sleep(rand)
        counter += 1
        print(f'{id} -> {counter}, random={rand}')

def main():
    process1 = Process(target=do_something, args=('ID1', ))
    process2 = Process(target=do_something, args=('ID2', ))
    process1.start()
    process2.start()    


if __name__ == '__main__':
    main()