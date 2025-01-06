import time
import random
def do_something(id):
    counter = 0
    while True:
        time.sleep(random.randint(1, 3))
        print(f'{id} -> {counter}')
        counter += 1
def main():
    do_something('Process 1')
    do_something('Process 2')

if __name__ == '__main__':
    main()