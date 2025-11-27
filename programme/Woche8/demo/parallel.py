import time
import random

from multiprocessing import Process
def do_something(id):
    counter = 0
    while counter < 10:
        print('sleeping...')
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)
        counter += 1
        print(f'sleep is over for {id}, sleep_time was: {sleep_time}, counter={counter}')

def mediator(function, id):
    function(id)

def main():
    p1 = Process(target=do_something, args=('ID1', ))
    p2 = Process(target=do_something, args=('ID2',))
    p1.start()
    p2.start()
    print('finished main')

if __name__ == '__main__':
    main()