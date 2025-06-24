import time
import random
from threading import Thread
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 5))
        counter += 1
        print(f'{id} -> {counter}')


def main():
    threads = []
    for i in range (1, 3):
        thread = Thread(target=do_something, args=[f'ID-{i}'])
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    print('done')
if __name__ == '__main__':
    main()