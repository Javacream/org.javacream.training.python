import time
import random
import multiprocessing
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 5))
        counter += 1
        print(f'{id} -> {counter}')


def main():
    process1 = multiprocessing.Process(target=do_something, args=['ID-1'])
    process2 = multiprocessing.Process(target=do_something, args=['ID-2'])
    process1.start()
    process2.start()
    print('done')
if __name__ == '__main__':
    main()