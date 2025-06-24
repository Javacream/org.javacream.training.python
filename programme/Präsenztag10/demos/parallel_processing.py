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
    processes = []
    for i in range (1, 3):
        process = Process(target=do_something, args=[f'ID-{i}'])
        process.start()
        processes.append(process)
    for p in processes:
        p.join()
    print('done')
if __name__ == '__main__':
    main()