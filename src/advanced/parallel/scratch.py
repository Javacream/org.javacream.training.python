from threading import Thread 
import time

COUNT = 25000000
def countdown(n):
    while n > 0:
        n = n - 1

start = time.time()


# t1 = Thread(target=countdown, args= (COUNT, ))
# t2 = Thread(target=countdown, args= (COUNT, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

countdown(2*COUNT)

end = time.time()
print(end - start)