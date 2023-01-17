from concurrent.futures import ProcessPoolExecutor, wait
import time

COUNT = 25000000
def countdown(n):
    while n > 0:
        n = n - 1
    return "Result"    

start = time.time()

with ProcessPoolExecutor(4) as executor:
    future1 = executor.submit(countdown, COUNT)
    future2 = executor.submit(countdown, COUNT)
    future3 = executor.submit(countdown, COUNT)
    future4 = executor.submit(countdown, COUNT)
    wait([future1, future2, future3, future4])
    print(future1.result())

end = time.time()
print(end - start)