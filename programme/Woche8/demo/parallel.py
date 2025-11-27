import time
import random

def do_something(id):
    counter = 0
    while True:
        print('sleeping...')
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)
        counter += 1
        print(f'sleep is over for {id}, sleep_time was: {sleep_time}, counter={counter}')

def mediator(function, id):
    function(id)

def main():
    mediator(do_something, 'ID1')
    mediator(do_something, 'ID2')
    print('finished main!')
main()